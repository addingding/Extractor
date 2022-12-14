from ecosys import *
from prots.roles._device import *


class aModbusServer(ABC):
    @abstractproperty
    def port(self)->int:...
    @abstractmethod
    def start(self):...
    @abstractmethod
    def stop(self):...
    
class aModbusTerminal(ABC):
    @abstractproperty
    def server():...
    @abstractproperty
    def address():...
