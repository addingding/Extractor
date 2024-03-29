from app.board import e_mt, e_stop, e_uv, e_work, info
from app.stage import application
from domains import (programer_widgets, start_widgets, status_widgets,
                     translators, uis)
from domains.machine import *
from domains.program.calib_widget import Calibration
from domains.program.custom_widget import CustomWidget, UpgradeWidget
from domains.program.machine_signals import MachineSignals
from domains.program.programs import programers
from domains.program.qthread_worker import *
from domains.uv_widget.uv_timer import timer_map, timers
from ecosys import *
from prots import *
from prots._cast import *

update_timer = QTimer()


splash = uis.splash_win()
flash = uis.flash_win()
infowin = uis.info_win()
window = uis.main_win()

program_handler = programers.program_handler()
program_io = CustomWidget(window)
upgrade_pg = UpgradeWidget(window)

app_worker = QWorker()

try:
    from domains.device.beeper import beepers
    beeper = call(beeper,beepers.get_beeper())
    logger.info("beeper loaded")
except Exception as e:
    logger.error(e)


uv_widget = timers.uv_widget(window,e_work,timer_map)
pg = programer_widgets.program_widget(window)
start_widget = start_widgets.start_widget(window)
window.program_updated.connect(start_widget.table_update)

translator_widget = translators.translator(window)
translator_widget.collect_tables(pg,start_widget)
translator_widget.trans_tables()

status_widget = status_widgets.status_widget(window,e_work, e_stop)
calib_widget = Calibration(window)


machine:Machine = call(machine,machines.get_machine())

uv_widget.uv = machine.uv
machine_signals = MachineSignals(machine)
status_widget.disk_key_pressed.connect(machine_signals.grid_pressed)
machine_signals.grid_arrived.connect(status_widget.disk_arrived_and_work_done)

status_widget.pause_signal.connect(machine.pause_pressed)
uv_widget.uv_stop_signal.connect(uv_widget.uv_pause)

status_widget.pause_signal.connect(status_widget.btn_pause_status_trans)
status_widget.stop_signal.connect(machine.stop_pressed)


emergency_timer = QTimer()
emergency_last_status = False

def emergency_check():
    global emergency_last_status
    _new_status = machine.door_safe.is_on
    if e_work.is_set() and emergency_last_status and (not _new_status): 
        if status_widget.btn_task_pause.isEnabled():
            logger.info("ermergency activated, pausing extracting")
            status_widget.pause_signal.emit(1)
        uv_widget.uv_stop_signal.emit(1)
    emergency_last_status = _new_status
    emergency_timer.start(300)

emergency_timer.timeout.connect(emergency_check)





def cast_enter():
    pass

def cast_exit():
    pass