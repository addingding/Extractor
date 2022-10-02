from ecosys import *

class aInput(ABC):
    @abstractproperty
    def is_on(self):...

class aSwitch(ABC):
    @abstractmethod
    def turn_on(self):...
    @abstractmethod
    def turn_off(self):...
    @abstractproperty
    def is_on(self):...
    @abstractmethod
    def switch(self):...

class aStepper():
    # clockwise, right direction
    @abstractproperty
    def ppr(self)->int:...
    @abstractproperty
    def position_p(self)->int:...     # pulse
    @abstractproperty
    def speed(self)->int:...    # pps

    # surely with right sensor limit
    # perhaps with left sernsor limit
    @abstractproperty
    def right_sensor(self)->bool:...
    @abstractproperty
    def left_sensor(self)->bool:...
    @abstractproperty
    def left_high(self)->bool:...
    @abstractproperty
    def at_home(self)->bool:...
    
    @abstractmethod
    def hard_stop():...

    # TODO
    # @abstractproperty
    # def exit(self):...
    # def __del__(self):
    #     self.exit()

class aScrew():
    @abstractproperty
    def upr(self)->float:              # unit per round
        pass
    @abstractproperty
    def position_u(self):         # units
        pass

class aMotion(ABC):
    @abstractmethod
    def rotate(self,pulses:int,accel_ms:int,speed:int,keep_sec:int):
        ...
    @abstractmethod
    def rotate_till(self,speed:int,direction_right:bool,sensor_right:bool,sensor_high:bool):
        ...
    @abstractmethod 
    def home_return(self):...

    @abstractmethod 
    def move_to(self):
        ...
    @abstractmethod
    def move(self,distance_u,accel_ms,speed_rpm,keep_sec):
        ...

class aThermo():
    @abstractproperty
    def temperature(self)->float:
        ...
    @abstractmethod
    def set_temperatrue(self)->float:
        ...

class aLed(aSwitch):
    pass
class aUV(aSwitch):
    @abstractproperty
    def uv(self):...
    pass
class aFan(aSwitch):
    pass

class aDoorSafe(aInput):
    pass
class aSheathSite(aInput):
    pass
class aReagentSite(aInput):
    pass


class HomeError(Exception):
    pass
class SafeError(Exception):
    pass

class aBeeper(ABC):
    @abstractmethod
    def beep(self):...
    @abstractmethod
    def on(self):...
    @abstractmethod
    def off(self):...
    
