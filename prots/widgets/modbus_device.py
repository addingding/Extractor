from prots.roles._modbus import *
from prots.roles._device import *

class aSensor(aInput):
    def __init__(self, address:int,site:int):
        super().__init__(address)
        self.site = site

class aRelay(aSwitch):
    def __init__(self, address:int,site:int):
        super().__init__(address)
        self.site = site

class aMThermo(aThermo):
    ...

class aMStepper(aModbusTerminal,aStepper):
    @abstractproperty
    def status(self)->dict:...
    #baud,current,speed,inited,pos,ppr
    @abstractmethod
    def _restore(self):...

    @abstractmethod
    def set_baud(self,baud):...
    @abstractmethod
    def set_current(self,work,stand):...
    @abstractmethod
    def set_speed(self):...
    @abstractmethod
    def back_zero(self):...
    @abstractmethod
    def go_rounds(self,rounds):...
