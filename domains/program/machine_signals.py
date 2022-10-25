from ecosys import *
from prots import *

class MachineSignals(QWidget):
    grid_arrived = Signal(int)
    def __init__(self, machine:aMachine) -> None:
        super().__init__()
        self.machine = machine

    def grid(self,n:int):
        if not self.machine.motor_stir.at_home:
            self.machine.motor_stir.home_direct()
        self.machine.motor_disk.grid(n)
        self.grid_arrived.emit(self.machine.motor_disk._grid)
    
    def update(self):
        self.machine.update()