from app.board import info
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

e_work = Event()
e_stop = Event()

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
    print("beeper loaded")
except Exception as e:
    print(e)


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
status_widget.pause_signal.connect(status_widget.btn_pause_status_trans)

status_widget.stop_signal.connect(machine.stop_pressed)

emergency_timer = QTimer()
def ermergency_check():
    print("-------- ermergency check -------- ")
    _last_status = False
    _new_status = machine.door_safe.is_on
    if \
       _last_status and (not _new_status):
        # e_work.is_set() and status_widget.btn_task_pause.isEnabled() and \
        print("ermergency activated")
        status_widget.pause_signal.emit(1)
    _last_status = _new_status
    emergency_timer.start(200)
emergency_timer.timeout.connect(ermergency_check)
emergency_timer.start(200)





def cast_enter():
    pass

def cast_exit():
    pass