from ecosys import *
from prots import *

class MachineSignals(QWidget):
    grid_arrived = Signal(int)
    def __init__(self, machine:aMachine) -> None:
        super().__init__()
        self.machine = machine

    def grid(self,n:int):
        self.machine.motor_disk.grid(n)
        self.grid_arrived.emit(n)
    
    def update(self):
        self.machine.update()