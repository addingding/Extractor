from prots.roles._device import *
from prots.roles._machine import *

TASK_STATUSES: list = ['new', 'assigned',
                       'working', 'paused', 'finished', 'canceled']


@dataclass
class aMove():
    stepper:str
    target:str
    accel_ms:int      # ms
    speed:int           # rpm
    keep_time:int       # seconds

@dataclass
class aOperation():
    idx:int
    op_name:str = "Operation"

    @abstractproperty
    def moves(self)->List[aMove]:...
    
@dataclass
class aStep():
    idx:int
    partition:int = 0
    operation_idx:int = 0

    @abstractproperty
    def operation(self)->aOperation:...

@dataclass
class aProgram():
    idx:int
    pg_name:str= "Program"
    steps:List[aStep]= field(default_factory=list)
    @abstractmethod
    def temperature_sets(self):...
@dataclass
class aTask():
    idx:str
    program:aProgram



class TestOperations():
    def test_operations(self):
        _move = aMove("motor_stir",234,600,30)
        print(_move)

if __name__=="__main__":
    T=TestOperations()
    T.test_operations()