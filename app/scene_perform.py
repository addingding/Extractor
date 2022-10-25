from ecosys import *
from app.cast import *

def prepare_task(a=None):
    if event_working.is_set():
        window.popup(about=("注意！","工作中，无法启动新任务！"))
        return
    if start_widget.selected_program is None:
        window.popup(about=(lang("Alert"),lang("choose one")))
        return
    
    print("prepare task")
    window.tabWidget.setCurrentIndex(0)
    start_widget.btn_start.setEnabled(False)
    status_widget.btn_task_start.setEnabled(True)
    status_widget.btn_task_start.clicked.connect(start_task)
    machine.motor_stir.prepare()

def start_task(a=None):
    if machine.sheath_sensor.is_on:
        window.popup(about=(lang("Alert"),lang("No sheath")) )
        return
    
    print("start task")
    status_widget.btn_task_start.setEnabled(False)
    machine.motor_stir.prepare_at_home()
    machine.motor_disk.home_return(timeout=15)
    machine.motor_disk.bottom()
    status_widget.btn_task_pause.setEnabled(True)
    
    
    global task_performer
    task_performer = TaskPerformer(_start_task,e_safe_perform,e_stop_perform)
    task_performer.signal_end.connect(task_end_notice)
    task_performer.signal_updated.connect(status_widget.update)
    task_performer.start()

def _start_task(e_safe:Event,e_stop:Event,signal_updated:Signal=None):
    event_working.set()
    e_stop.clear()
    task_program = start_widget.selected_program
    pg_idx = task_program.idx

    info["pg_idx"] = pg_idx
    info["pg_name"] = task_program.pg_name
    steps:list = start_widget.get_checked_steps()

    info["pg_total_time"] = total_pg_time(steps)
    info["pg_start_time"] = time.time()
    signal_updated.emit(1)

    info[f"disk_1_preset"] = 25
    info[f"disk_8_preset"] = 25
    machine.thermo_0.set_temperatrue(25)
    machine.thermo_1.set_temperatrue(25)

    set_temperature(steps,1)
    e_safe.wait()
    if not e_stop.is_set():
        run_task(e_safe,e_stop,signal_updated,machine,steps)
    event_working.clear()
    
def set_temperature(steps:list,step:int):
    assert step in [1,8]
    thermo = machine.thermo_0 if step==1 else machine.thermo_1
    for stp in steps:
        if int(stp[1])==step and stp[2]:
            op_idx = int(stp[2])
            op:Operation = operation_handler.obj(op_idx)
            t = op.temperature
            thermo.set_temperatrue(t)
            info[f"disk_{step}_preset"] = t

def total_pg_time(steps:list):
    t=0
    for step in steps:
        partition:int = int(step[1])
        operation_idx = int(step[2])
        operation:Operation = operation_handler.obj(operation_idx)
        t += operation.sec_mag
        t += operation.sec_mix
        t += operation.sec_wait
        t += 70 #HACK how to evaluate?
    return t

def run_task(e_safe,e_stop,signal_updated,machine:Machine,steps:list):
    for step in steps:
        partition:int = int(step[1])
        operation_idx = int(step[2])
        operation:Operation = operation_handler.obj(operation_idx)

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
                +operation.sec_wait+30,
            "step_start_time":time.time(),
            })
        signal_updated.emit(1)
        e_safe.wait()
        machine.perform_step(e_safe,partition,operation,step[0])
        if e_stop.is_set():
            break
    machine.task_end()
    info.update({
            "op_name":lang('Finshed'),
            })
    signal_updated.emit(1)
    
def task_end_notice(a=None):
    start_widget.table_update()
    message_known = Event()
    Thread(target=notify,args=(message_known,)).start()
    window.popup(about=(lang("attention"),lang('Finshed')+"!"))
    message_known.set()
    start_widget._selected_idx = None
    machine.motor_stir.prepare()
    start_widget.btn_start.setEnabled(True)


def notify(message_known:Event):
    while not message_known.is_set():
        beeper.on()
        time.sleep(0.5)
        beeper.off()
        time.sleep(0.5)
