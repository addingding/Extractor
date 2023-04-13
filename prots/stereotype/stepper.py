from ecosys import *
from prots.roles._device import aStepper,aScrew,aMotion

class Stepper(aStepper,aScrew,aMotion,ABC):
    def __init__(self,ppr,upr):
        self._ppr = ppr
        self._upr = upr
        self._speed = 60
        self._position = 0
        self._accel = 50
        self._keep = 0

    @property
    def ppr(self) -> int:
        return self._ppr
    @property
    def position_p(self) -> int:
        return self._position
    
    @property
    def speed(self):
        return self._speed

    def set_speed(self,value:float):
        self._speed = value
        
    @property
    def upr(self) -> float:
        return self._upr
    @property
    def ppu(self) -> float:
        return self._ppr/self._upr
    @property
    def position_u(self):
        return self._position/self.ppu
    @position_u.setter
    def position_u(self,value):
        self._position = int(value*self.ppu)
    
    @property
    def right_sensor(self) -> bool:
        return True
    @property
    def at_home(self) -> bool:
        return False
    
    @property
    def left_sensor(self) -> bool:
        return False
    @property
    def left_high(self) ->bool:
        return True
    
    def move_to(self,position_u,
        accel_ms=None,speed_rpm=None,keep_sec=None):
        distance_u = position_u - self.position_u
        self.move(distance_u,accel_ms,speed_rpm,keep_sec)
    
    def move(self,distance_u,
        accel_ms=None,speed_rpm=None,keep_sec=None):
        if not accel_ms is None:
            self._accel = accel_ms
        if not speed_rpm is None:
            self._speed = speed_rpm
        if not keep_sec is None:
            self._keep = keep_sec
        if not distance_u: return
        
        pulses = int(distance_u * self.ppu)
        self.rotate(pulses,accel_ms,speed_rpm,keep_sec)
        self._position += pulses
    @abstractmethod
    def home_return(self):
        self._position = 0
    
    def set_motor_aware(self,motor_aware:bool):
        self._motor_aware:aStepper = motor_aware
    @property
    def motion_safe(self):
        if hasattr(self,"_motor_aware"):
            return self._motor_aware.at_home
        else:
            return True