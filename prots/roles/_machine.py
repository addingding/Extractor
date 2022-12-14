from abc import *

from prots.roles._device import *
from prots.roles._modbus import aModbusServer
from prots.roles._operation import *


class aMachine(ABC):

    @abstractproperty
    def is_safe(self)->bool:...
    @abstractproperty
    def has_sheath(self)->bool:...
    @abstractproperty
    def has_reagent(self)->bool:...
    @abstractproperty
    def status_acting(self)->str:
        #"extracting","sterilizing","waiting","paused"
        ...

    @abstractproperty
    def motor_stir(self)->aStepper:... # 12 x0C
    @abstractproperty
    def motor_mag(self)->aStepper:... # 13 x0D
    @abstractproperty
    def motor_disk(self)->aStepper:... # 14 x0E
    @abstractproperty
    def motor_mask(self)->aStepper:... # 15 x0F

    @abstractproperty
    def thermo_master(self)->aThermo:...      # 11 x0B
    
    @abstractproperty
    def thermo_0(self)->aThermo:...      # 11 x0B
    @abstractproperty
    def thermo_1(self)->aThermo:...      # 11 x0B

    
    @abstractproperty
    def door_safe(self)->aDoorSafe:... # 10 x0A
    @abstractproperty
    def sheath_sensor(self)->aSheathSite:...
    @abstractproperty
    def reagent_sensor(self)->aReagentSite:...
    @abstractproperty
    def fan(self)->aFan:...
    @abstractproperty
    def led(self)->aLed:...
    @abstractproperty
    def uv(self)->aUV :...

    @abstractmethod
    def update(self):...
    
    @abstractmethod
    def self_check(self):...
    @abstractmethod
    def exit(self):...
    
    @abstractmethod
    def perform_step(self,step):
        ...
    @abstractmethod
    def perform_move(self,move):
        ...

class aEventBus(ABC):
    ...

if __name__=="__main__":
    amachine:aMachine = aSim(aMachine)
    amachine.server.start()
    print(amachine.server.port)