from app.cast import *
from ecosys import *


def prepare_task(a=None):
    if e_work.is_set():
        window.popup(about=(lang("Alert"),lang("Busy for new job.")))
        return
    pg = start_widget.selected_program
    if pg is None:
        window.popup(about=(lang("Alert"),lang("choose_one_program")))
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
    status_widget.btn_task_start.setChecked(True)
    status_widget.btn_task_start.clicked.connect(start_task, type=Qt.UniqueConnection)
    machine.motor_stir.prepare()
    set_temperature(1,25)
    set_temperature(8,25)

@Slot()
def start_task(a=None):
    logger.info("start task")

    if machine.sheath_sensor.is_on:
        logger.info("check sheath: no sheath")
        window.popup(about=(lang("Alert"),lang("No_sheath")) )
        return
    logger.info("check sheath: ok")

    if not info.get("door_at_spot"): #safe
        logger.info("check door: open. stop and return.")
        window.popup(about=(lang("Alert"),lang("close_the_door")) )
        return
    logger.info("check door: closed")
    

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
    status_widget.btn_task_start.setChecked(False)
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


    if not e_stop.is_set():
        run_task(e_stop,signal_updated,machine,steps)

def set_temperature(partition, t):
    if partition in [1,8]:
        info[f"disk_{partition}_preset"] = t
        thermo = machine.thermo_0 if partition==1 else machine.thermo_1
        Thread(target = thermo.set_temperatrue,args=(t,)).start()
        time.sleep(0.001)

def set_temperature_via_steps(partition:int,steps:list):
    if partition in [1,8]:
        t = get_preset_temperature(steps,partition)
        set_temperature(partition, t)
        logger.debug(f"{partition} temperatrue set to {t}")
def get_preset_temperature(steps:list,partition:int):
    t = 25
    for stp in steps:
        if int(stp[1])==partition and stp[2]:
            op:Operation = Operation(*stp[2])
            t = op.temperature
    return t


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
        logger.debug(f"partition {partition} start to go")
        operation:Operation = Operation(*step[2])

        if partition in [1,8]:
            set_temperature_via_steps(partition,steps)

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
            if partition in [1,8]:
                set_temperature(partition,25)
            break

        if partition in [1,8]:
            set_temperature(partition,25)

    machine.task_end()
    info.update({"op_name":lang('finshed'),})
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
    window.popup(about=(lang("Alert"),lang('finished')+"!"))
    message_known.set()
    
    set_task_start_sets(ends=True)
    start_widget._selected_idx = None
    machine.motor_stir.prepare()


def notify(message_known:Event):
    while not message_known.is_set():
        beeper.on()
        time.sleep(0.5)
        beeper.off()
        time.sleep(0.5)
