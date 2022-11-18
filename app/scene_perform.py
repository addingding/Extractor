from app.cast import *
from ecosys import *


def prepare_task(a=None):
    if e_work.is_set():
        window.popup(about=("注意！","工作中，无法启动新任务！"))
        return
    pg = start_widget.selected_program
    if pg is None:
        window.popup(about=(lang("Alert"),lang("choose one")))
        return
    else:
        ctx:List[Tuple[int,str]] = []
        for stp in pg.steps:
            ctx.append((int(stp[1]),str(stp[2][0]),int(stp[0])))
        info["disk_info"]=[""]*8
        for idx,txt,_stp in ctx:
            t = info["disk_info"][idx-1]
            if t != "":
                t = t +"\n"+ "_".join((str(_stp),txt))
            else:
                t = "_".join((str(_stp),txt))
            
            info["disk_info"][idx-1] = t
    
    logger.info("prepare task")
    window.tabWidget.setCurrentIndex(0)
    status_widget.btn_task_start.setEnabled(True)
    status_widget.btn_task_start.clicked.connect(start_task, type=Qt.UniqueConnection)
    machine.motor_stir.prepare()
    set_temperature_to_roomtemperature()

@Slot()
def start_task(a=None):
    if machine.sheath_sensor.is_on:
        window.popup(about=(lang("Alert"),lang("No sheath")) )
        return
    
    logger.info("start task")


    set_task_start_sets(True)
    
    machine.motor_stir.prepare_at_home()
    machine.motor_disk.home_return(timeout=15)
    machine.motor_disk.bottom()
    machine.motor_disk._grid = 1

    status_widget.btn_task_pause.setEnabled(True)
    status_widget.btn_task_stop.setEnabled(True)
    
    
    global task_performer
    global e_stop
    task_performer = TaskPerformer(perform_job,e_stop)
    task_performer.signal_end.connect(task_end_notice)
    task_performer.signal_updated.connect(status_widget.update)
    task_performer.start()

def set_task_start_sets(ends:bool=False):
    tabwidget:QTabWidget = window.tabWidget
    tabwidget.setTabEnabled(3,ends)
    tabwidget.setTabEnabled(4,ends)
    start_widget.btn_start.setEnabled(ends)
    status_widget.btn_task_start.setEnabled(False)

def perform_job(e_stop:Event,signal_updated:Signal=None):
    global e_work
    e_work.set()
    e_stop.clear()
    task_program = start_widget.selected_program
    pg_idx = task_program.idx

    info["pg_idx"] = pg_idx
    info["pg_name"] = task_program.pg_name
    steps:list = start_widget.get_checked_steps()

    info["pg_total_time"] = total_pg_time(steps)
    info["pg_start_time"] = time.time()
    signal_updated.emit(1)


    set_temperature(steps,1)
    if not e_stop.is_set():
        run_task(e_stop,signal_updated,machine,steps)

def _set_room_temperature():
    info[f"disk_1_preset"] = 25
    info[f"disk_8_preset"] = 25
    machine.thermo_0.set_temperatrue(25)
    machine.thermo_1.set_temperatrue(25)
def set_temperature_to_roomtemperature():
    Thread(target=_set_room_temperature).start()
    time.sleep(0.001)

def _set_temperatrue(steps:list,step:int):
    assert step in [1,8]
    thermo = machine.thermo_0 if step==1 else machine.thermo_1
    for stp in steps:
        if int(stp[1])==step and stp[2]:
            op:Operation = Operation(*stp[2])
            t = op.temperature
            thermo.set_temperatrue(t)
            info[f"disk_{step}_preset"] = t
def set_temperature(steps:list,step:int):
    Thread(target=_set_temperatrue,args=(steps,step)).start()
    time.sleep(0.001)

def total_pg_time(steps:list):
    t=0
    for step in steps:
        partition:int = int(step[1])
        operation:Operation = Operation(*step[2])
        t += operation.sec_mag
        t += operation.sec_mix
        t += operation.sec_wait
        t += 65 #HACK how to evaluate?
    return t

def run_task(e_stop,signal_updated,machine:Machine,steps:list):
    for step in steps:

        partition:int = int(step[1])
        operation:Operation = Operation(*step[2])

        if partition==8:
            set_temperature(steps,8)

        info.update({
            "step_idx": int(step[0]),
            "op_name":operation.op_name,
            "disk": partition,
            "sec_wait": operation.sec_wait,
            "sec_mix": operation.sec_mix,
            "sec_mag": operation.sec_mag,
            "ul_volumn": operation.ul_volumn,
            "speed_mix": operation.speed_mix,
            "temperature": operation.temperature,
            "step_total_time": operation.sec_mag
                +operation.sec_mix
                +operation.sec_wait+65,
            "step_start_time":time.time(),
            })
        signal_updated.emit(1)

        machine.perform_step(partition,operation,step[0])
        if machine.motor_stir._action_end.is_set():
            machine.motor_stir._action_end.clear()
            e_stop.set()
            break

    machine.task_end()
    info.update({
            "op_name":lang('finshed'),
            })
    signal_updated.emit(1)
    
def task_end_notice(a=None):
    e_work.clear()
    status_widget.btn_task_pause.setEnabled(False)
    status_widget.btn_task_start.setEnabled(False)
    status_widget.btn_task_stop.setEnabled(False)
    start_widget.btn_start.setEnabled(True)
    
    start_widget.table_update()
    message_known = Event()
    Thread(target=notify,args=(message_known,)).start()
    window.popup(about=(lang("attention"),lang('Finshed')+"!"))
    message_known.set()
    
    set_temperature_to_roomtemperature()
    set_task_start_sets(ends=True)
    start_widget._selected_idx = None
    machine.motor_stir.prepare()


def notify(message_known:Event):
    while not message_known.is_set():
        beeper.on()
        time.sleep(0.5)
        beeper.off()
        time.sleep(0.5)
