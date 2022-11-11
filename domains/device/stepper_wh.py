from ecosys import *
from prots import *
from domains.device.modbus import  *



PPR = 51200
def tuple_int(a,b):
    assert a in [1,0]
    assert b >= 0
    ab = 1-a*2
    return b*ab


class ModbusStepperDriver(ModbusTerminal):
    def __init__(self, id: str, server: RtuServer, address: int):
        super().__init__(id, server, address)
        self._position = 0

    def _change_address(self,addr:int):
        return self.set_single(0x0020,addr)
    def _verify_address(self):
        return super()._verify_address()

    def _set_current(self,current:int=16,standby:int=1):
        if current >31: current =31
        _current = (current<<8) + standby
        self.set_single(0x0023,_current)
    
    def _set_baud(self,baud:int):
        self.set_many(0x0021,2,baud)
    def _set_back_zero_speed(self,speed=PPR*1):
        self.set_many(0x0024,2,speed)
    def _set_run_speed(self,speed=PPR*1):
        self.set_many(0x0026,2,speed)
    def _set_running_speed(self,speed=PPR*1):
        self.set_many(0x0028,2,speed)
    
    def _restore(self):
        _set_zero = 1
        right_direction = 1 #更改硬件设置传感器LR以及电机B+B-以对应
        _at_home = 0  
        _left_low = 0
        _right_enabled = 1
        _left_enanbled = 1 
        code = (_set_zero<<12)+(right_direction<<4)+(_at_home<<3)+(_left_low<<2)+\
            (_right_enabled<<1)+(_left_enanbled)
        time.sleep(0.05)
        self.set_single(0x002A,code)
        time.sleep(0.1)

    def _rotate_to(self,cw,at_home,left_low,right_enabled,left_enabled,position_pulse):
        assert position_pulse>=0
        b_pulses = binstring(abs(position_pulse),25)
        _position_high = int(b_pulses[0],2)
        _position_low = int(b_pulses[1:],2)

        msg = (cw<<31)+(at_home<<27)+(at_home<<26)\
            +(right_enabled<<25)+(left_enabled<<24)+(_position_high<<28)+(_position_low)
        time.sleep(0.05)
        self.set_many(0x002B,2,msg)
        return

    def move_till(self,cw:bool,high:bool,enabled:bool=True):
        set_zero = False
        code = (set_zero<<12)+(cw<<4)+(high<<3)+(high<<2)+(enabled<<1)+(enabled) #使能,光电才生效
        time.sleep(0.1)
        self.set_single(0x002A,code)

    @property
    def position(self)->int:
        ret = 0
        r = None
        t = 0
        try:
            while r is None:
                t += 1
                r = self.query(0x002B,2)
                if r is None:
                    if t < 10: 
                        time.sleep(0.1)
                        continue
                    else:
                        ret = 0
                else:
                    _r = binstring(r[0],16)+binstring(r[1],16)
                    _d = int(_r[0],2)
                    _p = int(_r[-28]+_r[-24:],2)
                    ret = tuple_int(_d,_p)
        except Exception as e:
            print(self.id,"_position_query",e)
            return 0
        return ret

    def _stop(self,power_stop=False):
        # time.sleep(0.05)
        self.set_single(0x002D,power_stop)
    
    @property
    def _status(self):
        i = 10
        while i>0:
            try:
                s = self.query(0x002E,1)
            except Exception as e:
                print("status get error",e)
                time.sleep(0.1)
                continue

            if s is None:
                time.sleep(0.1)
                continue
            elif isinstance(s,tuple):
                    s=s[0]
            s = int(s)
            
            status = dict(
                stopped = bin_get(s,15),
                over_heat = bin_get(s,14),
                # over120 = bin_get(s,14),
                # over136 = bin_get(s,13),
                left_low = bin_get(s,0),
                at_home = bin_get(s,1),
                current = ((s - ((s>>8)<<8))>>4)
                )
            return status

    def _query_speed(self):
        _r = self.query(0x0028,2)
        if isinstance(_r,tuple) and len(_r)>0:
            return _r [0]
    def set_baud(self):
        return self._set_baud(115200)
    def set_current(self,current=16,standby=1):
        return self._set_current(current,standby)
    def local_set_speed(self,speed_float):
        speed_p = int(PPR*speed_float)
        self._set_running_speed(speed_p)
        self._set_back_zero_speed(speed_p)
        self._set_run_speed(speed_p)


class ModbusStepper(ModbusStepperDriver,Stepper):
    def __init__(self,id: str, server: RtuServer, address: int,ppr:int,upr:float):
        super().__init__(id,server,address)
        Stepper.__init__(self,ppr,upr)
        self.name = self.id
        time.sleep(0.2)
        self._wait_ignore = Event()

        # self.set_baud()
        self.set_current(15) # (n=15+1)/16 A
        self.local_set_speed(1)
        time.sleep(0.2)

    @property
    def at_home(self) -> bool:
        return self._status.get("at_home")

  
    def rotate(self, pulses: int, accel_ms: int, speed: int, keep_sec: int):
        self.rotate_no_wait(pulses)
        self._wait_until_stopped()

    def rotate_no_wait(self, pulses):
        _pulses = self.position + pulses
        _cw = 0 if _pulses >0 else 1 
        _point = abs(_pulses)
        self._rotate_to(_cw,False,False,False,False,_point)



    def rotate_till(self, speed: int, direction_right: bool, sensor_right: bool, sensor_high: bool):
        return super().rotate_till(speed, direction_right, sensor_right, sensor_high)

    def _back_zero(self,timeout = 15):
        print(self.name,"back_zero:",datetime.datetime.now())
        _status = self._status
        if _status is None:
            time.sleep(1)
            print(self.name,"no return, retry...")
            self._back_zero(timeout)
        else:
            if not self.at_home:
                print(self.name,"hard home return")
                self._restore()
            else:
                print(self.name,"just right_at_home")
        self._wait_until_stopped(timeout)
        if not self.at_home:
            self._back_zero()
            
        self._assert_zero_point()
        self.current_point = 0

    def _assert_zero_point(self):
        if not self.at_home:
            print(self.name,"HomeError")
            raise HomeError

    def is_stopped(self):
        return self._status.get("stopped")

    def _wait_until_stopped(self,timeout=None):
        time.sleep(1)
        if not timeout is None:
            timeout -= 1
        t = 0
        while True:
            try:
                if self.is_stopped():
                    t += 1
                    if t>=3:
                        print("motor stopped")
                        break
                time.sleep(0.1)
                if not timeout is None:
                    timeout -= 0.1
                    if timeout<=0:
                        raise TimeoutError
            except Exception as e:
                print(self.name,e)



    def home_return(self,timeout=15):
        if self.motion_safe:
            self._back_zero(timeout)
            self._position = 0
        else:
            print(self.name,"not sure to move safely ")
            raise SafeError

    def set_points(self,ul,bottom_u:float):
        self._bottom = -abs(bottom_u)

    def bottom(self):
        if self.motion_safe:
            self.move_to(self._bottom)
        else:
            print("not sure to move safely ")
            raise SafeError
    def home(self):
        self.move_to(0)
        self.home_return()
    def hard_stop(self):
        self._stop(power_stop=True)
    def soft_stop(self):
        self._stop(power_stop=False)

    def calibrate(self):
        self.set_speed(0.2)
        time.sleep(0.5)
        pos_before = self.position
        # self.home_return() # self.position==0
        self.move_till(True,False,True)
        self._wait_until_stopped()
        self.soft_stop()
        pos_after = self.position
        print("before",pos_before,"after",pos_after)
        delta_p = pos_after-pos_before
        delta_u = delta_p/self.ppu
        print("distance_p return",delta_p)

        self.position_u = 0
        self.move(-delta_u)
        self.position_u = 0
        self.set_speed(5)

        return delta_p


class DiskMotor(ModbusStepper):
    def __init__(self, id: str, server: RtuServer, address: int, ppr: int, upr: float):
        ModbusStepper.__init__(self,id, server, address, ppr, upr)
        self._grid = 1

        self.action_stop = Event()
        self.signal_ignore = Event()
        self._target = None

        self.set_current(19,4) # (n=15+1)/16 A
        self.local_set_speed(1)


    def grid_cw(self):
        self.grid(self._grid+1)
    def grid_ccw(self):
        self.grid(self._grid-1)
    def prepare_at_grid_1(self):
        self.home_return()
        self.bottom()
        self._grid = 1

    def grid(self,site:int):
        print("grid",site)
        if self.action_stop.is_set():
            return
        self._target = site
        if not self.motion_safe:
            print("not safe for motion, please check the stir_motor")
            raise(SafeError)
        elif 1<= site <=8:
            self.grid_move(site)
    def grid_move(self,site:int):

        _point = self.signal_to_site(site)
        self.signal_ignore.set()
        ret = self.wait_grid_move_end(_point)

        if ret:
            self._grid = self._target
            self._target = None
            return True
        else:
            return False

    def wait_grid_move_end(self,point:int):
        while True:
            if self.action_stop.is_set():
                return False
            self.signal_ignore.wait()
            time.sleep(0.01)
            if self.is_stopped() and abs(point-abs(self.position))<20: # 
                return True
            else:
                pass #TODO 如果位置不正确，如何返回？

    def signal_to_site(self, site:int):
        _point = int(self.ppu*(site-1+abs(self._bottom)))
        self._rotate_to(True,False,False,False,False,_point)
        return _point

    def pause(self):
        self.signal_ignore.clear()
        time.sleep(0.05)
        self.soft_stop()
        self.signal_ignore.set()
    def resume(self):
        self.signal_ignore.clear()
        time.sleep(0.01)
        if self._target is not None:
            self.signal_to_site(self._target)
        self.signal_ignore.set()
    def stop(self):
        self.pause()
        time.sleep(0.5)
        self.action_stop.set()
        time.sleep(1)
        self.prepare_at_grid_1()
        self.action_stop.clear()


        


class WhSteppers:
    def get_stepper_wh(self,name,server,address,ppr,upr):
        return ModbusStepper(name,server,address,ppr,upr)
    def get_stepper_mag(self,name,server,address,ppr,upr):
        return ModbusStepper(name,server,address,ppr,upr)
    def get_stepper_mask(self,name,server,address,ppr,upr):
        return ModbusStepper(name,server,address,ppr,upr)
    def get_stepper_disk(self,name,server,address,ppr,upr):
        return DiskMotor(name,server,address,ppr,upr)
    
wh_steppers = WhSteppers()


class ModbusStepperTest():

    def __init__(self):

        server = servers.get_modbus_server("COM4" if sys.platform.startswith('win') else "/dev/ttySC1")

        self.server = server

        self.motor_disk = DiskMotor('motor_disk',self.server,13,51200,0.4447323292111213) #0.25pie
        # self.motor_mag = ModbusStepper('motor_mag',self.server,14,51200,4)
        # self.motor_mask = ModbusStepper('motor_mask',self.server,15,51200,2)
        # self.steppers:List[ModbusStepper] = [self.motor_mag,self.motor_disk,self.motor_mask]

        from app.board import defaults
        self.motor_disk.set_points(0, defaults.get("motor_bottom").get("motor_disk"))

    # def __del__(self):
    #     self.switches.turn_off(2)
    #     print(self.switches.read_out())

    #     self.switches.exit()

    def test_motor_disk(self):
        self.motor_disk.prepare_at_grid_1()
        tm = Thread(target=self.thread_move)
        tm.start()
        time.sleep(2)
        Thread(target=self.thread_pause).start()
        time.sleep(2)
        Thread(target=self.thread_resume).start()
        time.sleep(2)
        Thread(target=self.thread_pause).start()
        time.sleep(2)
        Thread(target=self.thread_resume).start()
        time.sleep(1)
        ts = Thread(target=self.thread_stop)
        ts.start()

    def thread_move(self):
        self.motor_disk.grid(5)
        self.motor_disk.grid(2)
    def thread_pause(self):
        self.motor_disk.pause()
        print('pause finished')
    def thread_resume(self):
        self.motor_disk.resume()
        print('resume finished')
    def thread_stop(self):
        self.motor_disk.stop()
        print('stop finished')

    def test_signal(self):
        for stepper in self.steppers:
            print(stepper.name,"right:",stepper.at_home)


    def test_home(self):
        for stepper in self.steppers:
            stepper.home_return()

    def test_calibrate(self):
        self.motor_disk.calibrate()
        # self.motor_mag.calibrate()

    def test_stepper(self):

        self.stepper._stop()
        time.sleep(0.1)
      
        # self.stepper.move_to(30)
        # time.sleep(5)
        for i in range(10):
            self.stepper.move_till(cw=1,high=True,enabled=False)
            time.sleep(0.5)
            self.stepper._stop()
            self.stepper.move_till(cw=0,high=True,enabled=False)
            time.sleep(0.5)
            self.stepper._stop()
        self.stepper.local_set_speed(0)
        time.sleep(1)
        self.stepper._stop()
        time.sleep(1)
        self.stepper.server.close()

    def test_stepper_pos(self):

        self.stepper._stop()
        time.sleep(0.1)
      
        time.sleep(2)
        for i in range(20):
            self.stepper._move_to_pulse(2000)
            self.stepper._move_to_pulse(0)
        self.stepper.local_set_speed(0)
        time.sleep(1)
        self.stepper._stop()
        time.sleep(1)
        self.stepper.server.close()


    def print_status(self,stp):
        for i in range(10):
            print(stp._status)
            time.sleep(0.5)
    def thread_test_modbus_excution(self):
        tax = Thread(target=self.print_status,args=(self.stepper,))
        tax.start()
        time.sleep(10)
        tax.join()

    def thread_test_back_zero(self):
        tbx = Thread(target=self.stepper.back_zero)
        tbx.start()
        tbx.join()

    def test_mag_speed(self):
        self.motor_mag.local_set_speed(8)
        time.sleep(1)
        self.motor_mag.home()
        self.motor_mag.move_to(-50)
        self.motor_mag.move_to(-5)
        self.motor_mag.home()
def main():
    T = ModbusStepperTest()
    T.test_motor_disk()
    # T.test_signal()
    # T.test_home()
    # T.test_calibrate()
    # T.test_mag_speed()
if __name__ == "__main__":
    main()