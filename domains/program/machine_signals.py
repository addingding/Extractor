from ecosys import *
from prots import *

class MachineSignals(QWidget):
    grid_arrived = Signal(int)
    def __init__(self, machine:aMachine) -> None:
        super().__init__()
        self.machine = machine

    def grid_pressed(self,n:int):
        Thread(target= self._grid_pressed,args=(n,self.grid_arrived)).start()
        # self.grid_arrived.emit(n) #XXX self.machine.motor_disk._grid 

    def _grid_pressed(self,n:int,signal):
        if not self.machine.motor_stir.at_home:
            self.machine.motor_stir.home_direct()
        self.machine.motor_disk.grid(n)
        signal.emit(n)
    
    def update(self):
        self.machine.update()