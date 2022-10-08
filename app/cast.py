from ecosys import *
from prots import *

from app.stage import application
from app.board import info

from domains import uis,programer_widgets,start_widgets
from domains import translators
from domains import status_widgets
from domains.uv_widget.uv_timer import timers,timer_map
from domains.machine import *
from domains.program.programs import programers
from domains.program.calib_widget import Calibration
from domains.program.machine_signals import MachineSignals
from domains.program.qthread_worker import *
from domains.program.custom_widget import CustomWidget,UpgradeWidget

from prots._cast import *

event_working = Event()
e_safe_perform = Event()
e_stop_perform = Event()

update_timer = QTimer()

splash = uis.splash_win()
flash = uis.flash_win()
window = uis.main_win()

program_handler = programers.program_handler()
operation_handler = programers.operation_handler()
program_io = CustomWidget(window)
upgrade_pg = UpgradeWidget(window)

app_worker = TempWorker()

try:
    from domains.device.beeper import beepers
    beeper = call(beeper,beepers.get_beeper())
    print("load",beeper)
except Exception as e:
    print(e)


uv_widget = timers.uv_widget(window,event_working,timer_map)
pg = programer_widgets.program_widget(window)
op = programer_widgets.operation_widget(window)
start_widget = start_widgets.start_widget(window)
window.program_updated.connect(start_widget.table_update)

translator_widget = translators.translator(window)
translator_widget.collect_tables(pg,op,start_widget)
translator_widget.trans_tables()

status_widget = status_widgets.status_widget(window,event_working,e_safe_perform, e_stop_perform)
calib_widget = Calibration(window)


machine:Machine = call(machine,machines.get_machine())

uv_widget.uv = machine.uv
machine_signals = MachineSignals(machine)
status_widget.disk_key_pressed.connect(machine_signals.grid)
machine_signals.grid_arrived.connect(status_widget.disk_arrived_and_work_done)







def cast_enter():
    pass

def cast_exit():
    pass