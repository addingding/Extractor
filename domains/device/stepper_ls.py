from ecosys import *
from prots import *
from app.board import defaults
from domains.device.modbus import  *
from domains.uv_widget.uv_timer import JobTimer

PointMode = namedtuple("PointMode","type_03 insert_4 ovlp_5 abspos_6 jump_pnt813 jump_14")
def mode_to_number(p:PointMode):
    return p.type_03+(p.insert_4<<4)+(p.ovlp_5<<5)+(p.abspos_6<<6)+(p.jump_pnt813<<8)+(p.jump_14<<14)

sPoint = namedtuple("sPoint","mode pos_h pos_l speed acc_time dacc_time interval")

standard_mode = mode_to_number(PointMode(1,0,0,0,0,0))

stir_mode_top = mode_to_number(PointMode(1,1,0,0,5,1))  #4
stir_mode_btm = mode_to_number(PointMode(1,1,0,0,4,1))  #5

default_point = sPoint(0,0,0,200,20,20,1)


def high_low_number(n):
    hight = n>> 16
    low = n &((1<<16)-1)
    return hight,low

class LsStepperDriver(ModbusTerminal):
    def __init__(self, name: str, server: RtuServer, address: int):
        super().__init__(name, server, address)
        self.points = {}
        self.enable_io()
        self.pr_control_set()
        self.set_max_current(15)

    def set_zero_threshold(self):
        self.set_single(0x0175,10)

    def enable_io(self):
        self.set_single(0x000F,1)
        self.set_single(0x0147,0xA5)    #di2 limit 常闭

    def pr_set_back_zero_mode(self):
        self.set_single(0x600A,0x01)
    def pr_start_back_zero(self):
        self.set_single(0x6002,0x20)
    
    def set_current_point_0(self):
        self.set_single(0x6002,0x21)

    def speed_run(self,speed:int):
        if speed<600:
            self.set_single(0x6200,0x0002)  #speed mode
            self.set_single(0x6203,speed)   #set_speed
            self.set_single(0x6002,0x0010)  #triger
    def speed_stop(self):
        self.set_single(0x6002,0x0040)
    def soft_stop(self):
        self.speed_stop()
        self.set_max_current(0)

    def read_input(self,n=1):
        assert 0<= n<= 6
        return (self.query(0x0179,1)[0] & (1<<n))>>n
    @property
    def right_light_is_on(self):
        return self.read_input(1)


    @property
    def high_pos(self):
        # return self.query(0x6201,1)[0]
        return self.query(0x602A,1)[0]
    @property
    def low_pos(self):
        return self.query(0x602B,1)[0]
        # return self.query(0x6202,1)[0]

    @property
    def position(self):
        return (self.high_pos<<16)+self.low_pos

    def set_back_zero_speed(self):
        self.set_single(0x600F,10) # back_zero high_speed
        self.set_single(0x6010,1)  # back_zero low_speed

    def save_settings(self):
        self.set_single(0x1801,0x2211)
    def reset_settings(self):
        self.set_single(0x1801,0x2233)

    def set_max_current(self,cur=10):
        if cur<=30:
            self.set_single(0x0191,cur)
            # self.set_single(0x0195,10) #额定电流
            # self.set_single(0x0197,10) #锁轴电流

    def set_ppr(self,ppr=10000):
        assert 200<=ppr<=51200
        self.set_single(0x1001,ppr)

    def jog(self,right):
        self.set_single(0x1801,0x4001+right)
    def pr_control_set(self,ctrg:bool=0,soft:bool=1,open_on:bool=0,level:bool=0):
        pr = (level<<4)+(open_on<<2)+(soft<<1)+ctrg
        self.set_single(0x6000,pr)
    
    def activate_positioning(self,site:int):
        self.set_single(0x6002,0x10+site)
        self.wait_positioned()
    def activate_positioning_without_wait(self,site:int):
        self.set_single(0x6002,0x10+site)

    def wait_positioned(self):
        while True:
            try:
                r = self.query(0x6002,1)
                if r is not None:
                    t = r[0]
                    if (t is not None) and (not t):
                        return
            except Exception as e:
                print(e)

    def point_set(self,site:int,point:sPoint=None):
        assert 0<=site<=16
        if point is None:
            point = self.points.get(site,default_point)
        self.points[str(site)] = point
        for i in range(8):
            self.set_single(0x6200+site*8,point.mode)
            self.set_single(0x6201+site*8,point.pos_h)
            self.set_single(0x6202+site*8,point.pos_l)
            self.set_single(0x6203+site*8,point.speed)
            self.set_single(0x6204+site*8,point.acc_time)
            self.set_single(0x6205+site*8,point.dacc_time)
            self.set_single(0x6206+site*8,point.interval)

        
class LsStepper(Stepper):
    def __init__(self,name: str, server: RtuServer, address: int,ppr:int,upr:float) -> None:
        super().__init__(ppr,upr)
        self.driver:LsStepperDriver = LsStepperDriver(name, server, address)

    def drop_before_calibrate(self):
        self.driver.set_max_current(0)
        time.sleep(6)

    def calibrate(self):
        self.driver.set_current_point_0()
        self.driver.set_max_current(10)

        while not self.driver.right_light_is_on:
            self.driver.speed_run(30)
        self.driver.speed_stop()
        pos_p = self.driver.position
        self.driver.set_current_point_0()

        d=5
        self.set_points(200,d)
        self.bottom()
        self.driver.set_current_point_0()

        while not self.driver.right_light_is_on:
            self.driver.speed_run(1)
        self.driver.speed_stop()
        _p = self.driver.position
        self.driver.set_current_point_0()


        pos_p = pos_p - (int(self.ppu*d) - _p)
        print("distance return:",pos_p,'\bp')
        return pos_p

    def rotate(self, pulses: int, accel_ms: int, speed: int, keep_sec: int):
        self.driver.point_set(pulses)
        return super().rotate(pulses, accel_ms, speed, keep_sec)
    def rotate_till(self, speed: int, direction_right: bool, sensor_right: bool, sensor_high: bool):
        return super().rotate_till(speed, direction_right, sensor_right, sensor_high)
    def home_return(self):
        self.driver.set_max_current(15)
        self.driver.set_back_zero_speed()
        self.driver.pr_set_back_zero_mode()
        self.driver.pr_start_back_zero()
        self.driver.wait_positioned()
        return 


    def set_points(self,ul:float,bottom_u:float,
            stir_accel_ms = 100,stir_speed_rpm = 240):

        beads_distance = defaults.get("beads_distance",0)
        bottom_u = abs(bottom_u)- beads_distance

        if ul<=100: 
            level_mm = 7*ul/100
            stir_mm = 3
        else:
            level_mm = 2*ul/100+5
            stir_mm = 7

        p_home = 0
        p_bottom = int(bottom_u*self.ppu)
        p_liquid = int((bottom_u-level_mm)*self.ppu)
        p_half = int((bottom_u-level_mm/2)*self.ppu)
        p_stir = int((bottom_u-stir_mm)*self.ppu)
        

        sp_home = sPoint(standard_mode,*high_low_number(p_home),30,100,100,100)
        sp_liquid = sPoint(standard_mode,*high_low_number(-p_liquid),30,100,100,100)

        sp_liquid_inner = sPoint(standard_mode,*high_low_number(-p_liquid),2,100,100,100)
        sp_half = sPoint(standard_mode,*high_low_number(-p_half),2,100,100,100)
        sp_stir_end = sPoint(standard_mode,*high_low_number(-p_half),2,100,100,100)
        sp_bottom = sPoint(standard_mode,*high_low_number(-p_bottom),1,100,100,100)

        sp_stir_top = sPoint(stir_mode_top,*high_low_number(-p_stir),stir_speed_rpm,stir_accel_ms,stir_accel_ms,1)
        sp_stir_bottom = sPoint(stir_mode_btm,*high_low_number(-p_bottom),stir_speed_rpm,stir_accel_ms,stir_accel_ms,1)

        self.driver.point_set(1,sp_liquid_inner)
        self.driver.point_set(2,sp_half)
        self.driver.point_set(3,sp_bottom)
        self.driver.point_set(6,sp_stir_end)

        self.driver.point_set(4,sp_stir_top)
        self.driver.point_set(5,sp_stir_bottom)

        self.driver.point_set(7,sp_home)
        self.driver.point_set(8,sp_liquid)

    def bottom(self):
        self.driver.activate_positioning(3)

    def bottom_mag(self,mag_sec):
        self.bottom()
        time.sleep(mag_sec)
    @property
    def at_home(self) -> bool:
        return self.driver.right_light_is_on
    def home(self):
        self.driver.activate_positioning(1)
        self.driver.activate_positioning(7)

    def stir_mix(self,e_safe:Event,mix_sec):
        if mix_sec<=0: return
        self.driver.set_max_current(20)
        self.stir_time = Event()

        
        self.driver.activate_positioning_without_wait(5)
        self.stir_time.wait(mix_sec)

        self.driver.speed_stop()
        self.driver.speed_stop()
        self.driver.speed_stop()
        self.driver.set_max_current(10)



    def liquid_wait(self,keep_sec):
        self.outer_liquid()
        if keep_sec>0:
            time.sleep(keep_sec)

    def inner_liquid(self):
        self.driver.activate_positioning(1)
    def outer_liquid(self):
        self.driver.activate_positioning(8)

    def half_liquid(self):
        self.driver.activate_positioning(2)
    def hard_stop(self):
        self.driver.soft_stop()

class LsSteppers:
    def get_stepper_ls(self,name,server,address,ppr,upr):
        return LsStepper(name,server,address,ppr,upr)
    
ls_steppers = LsSteppers()

class TestLs:
    def __init__(self):
        from domains.device.modbus_switch import switches

        self.server = servers.get_modbus_server("COM4" if sys.platform.startswith('win') else "/dev/ttyAMA1")

        sw = switches.get_ios("ios",self.server,1)
        led = switches.get_switch(sw,0)
        led.turn_on()
        self.stopper = switches.get_switch(sw,3)
        
        self.stepper = ls_steppers.get_stepper_ls("LsStepper",self.server,12,10000,60)
        self.driver = self.stepper.driver
        self.stepper.home_return()
        
        # self.stepper.set_points(100,75)
    def __del__(self):
        self.server.close()

    def test_direction(self):
        self.driver.set_max_current(15)
        self.driver.speed_run(60)
        time.sleep(2)
        self.driver.speed_stop()

    def test_speed(self):
        self.driver.set_max_current(10)
        mode_int = standard_mode
        accel_ms = 20
        speed = 60
        position_p = 20000
        point_0 = sPoint(mode_int,0,position_p,speed,accel_ms,accel_ms,1)
        point_1 = sPoint(mode_int,0,0,speed,accel_ms,accel_ms,1)
        self.driver.point_set(0,point_0)
        self.driver.point_set(1,point_1)
        time.sleep(0.5)

        self.driver.activate_positioning(0)
        self.driver.activate_positioning(1)



    def test_motion(self):
        self.driver.set_current_point_0()
        self.driver.set_max_current(10)
        mode_int = standard_mode
        accel_ms = 20
        speed_rpm = 30
        position_p = 0
        distance_p = 5000 #60mm/10000p
        hl_pos = high_low_number(position_p+distance_p)

        mode_0 = mode_to_number(PointMode(1,0,0,0,0,0))
        point_0 = sPoint(mode_0,0,position_p,speed_rpm,accel_ms,accel_ms,1)
        self.driver.point_set(0,point_0)

        mode_1 = mode_to_number(PointMode(1,0,0,0,0,0))
        point_1 = sPoint(mode_1,0,position_p+distance_p,speed_rpm,accel_ms,accel_ms,1)
        self.driver.point_set(1,point_1)

        # mode_stop = mode_to_number(PointMode(0,0,0,0,0,0))
        # point_stop = sPoint(mode_stop,0,0,speed_rpm,accel_ms,accel_ms,1)
        # self.driver.point_set(15,point_stop)
        
        time.sleep(0.5)

        self.driver.activate_positioning(1)
        # self.driver.activate_positioning(0)

    def test_stir(self):
        self.driver.set_max_current(20)
        mode_int = standard_mode
        accel_ms = 100 #50
        speed_rpm = 100 #300
        position_p = -5000
        distance_p = 600

        mode_a = mode_to_number(PointMode(1,0,0,0,0,0))
        point_a = sPoint(mode_a,*high_low_number(position_p),speed_rpm,accel_ms,accel_ms,1)
        self.driver.point_set(9,point_a)

        mode_0 = mode_to_number(PointMode(1,1,0,0,11,1))
        point_0 = sPoint(mode_0,*high_low_number(position_p),speed_rpm,accel_ms,accel_ms,10)
        self.driver.point_set(10,point_0)

        mode_1 = mode_to_number(PointMode(1,1,0,0,10,1))
        point_1 = sPoint(mode_1,*high_low_number(position_p+distance_p),speed_rpm,accel_ms,accel_ms,10)
        self.driver.point_set(11,point_1)

        time.sleep(0.5)

        t = time.time()
        ts = 100
        self.driver.activate_positioning(9)
        self.driver.activate_positioning_without_wait(11)
        time.sleep(3)
        self.stopper.turn_on()
        # self.driver.activate_positioning(9)
        # self.driver.speed_stop()
        time.sleep(3)
        self.stopper.turn_off()
        # for i in range(ts):
        #     self.driver.activate_positioning(11)
        # dt = time.time()-t
        
        # print(int(ts/dt),"Hz")
        self.stepper.home()

    def read_light_limit(self):
        print("right_light_limit",self.driver.right_light_is_on)

    def test_home_return_and_stir(self):
        self.driver.set_max_current(10)
        time.sleep(1)
        T.stepper.home_return()

        T.stepper.set_points(100,60)

        T.stepper.bottom_mag(1)
        print(self.driver.position/self.stepper.ppu)
        a = 400
        for i in range(a):
            T.stepper.driver.activate_positioning(5)
    
    def test_calibration(self):
        self.stepper.drop_before_calibrate()
        pos = self.stepper.calibrate()
        # print("bottom detected at:",pos,"\bp")
    def test_mix_sec(self):
        self.stepper.stir_mix(10)

if __name__ == "__main__":
    T = TestLs()
    # T.test_jog()

    driver = T.stepper.driver
    # T.test_motion()
    # T.test_stir()
    # T.test_speed()
    # T.test_direction()
    # T.read_light_limit()
    
    # T.test_calibration()
    # time.sleep(1)
    # T.test_stir()
    # T.test_home_return_and_stir()

    # T.test_mix_sec()
    
    
