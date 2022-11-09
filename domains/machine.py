from prots import *
from app.board import *
from app.board import info

from domains.device import *
from domains.program import *
from domains.device.modbus import servers

from domains.device.stepper_ls import *
from domains.device.stepper_wh import *
from domains.device.modbus_switch import *
from domains.device.modbus_thermo import *
from domains.uv_widget.uv_timer import *
from domains.program.programs import *

dm= defaults.get("device_map")

moves_ready = (
    ("z","home"),
    ("v","bottom"),
    ("y","bottom"),
    ("x","part_n"),
    ("y","home"),
    ("z","liquid_wait"))
moves_first = [
    ("z","bottom_mag"),
    ]
moves_stir =[
    ("z","half_liquid"),
    ("v","home"),
    ("z","stir_mix"),
    ("z","inner_liquid")
    ]
moves_leave =[
    ("v","bottom"),
    ("z","bottom_mag"),
    ("z","inner_liquid")
    ]
moves_end =[
    ("z","home"),
    ("v","home")
    ]

class MachineMain(aMachine):
    def __init__(self,devices) -> None:
        self.devices = devices
        self._status_acting:str = "waiting" 
        self.threads:List[Thread] = list()
        self._available = Event()
        self._emergency = Event()
        self.job_timer = timers.job_timer()
        
        self.sleep = time.sleep

    @property
    def motor_stir(self) -> Union[aStepper,LsStepper]:
        return self.devices.get("_motor_stir")
    @property
    def motor_mag(self) -> Union[aStepper,ModbusStepper]:
        return self.devices.get("_motor_mag")
    @property
    def motor_disk(self) -> Union[aStepper,DiskMotor]:
        return self.devices.get("_motor_disk")
    @property
    def motor_mask(self) -> Union[aStepper,ModbusStepper]:
        return self.devices.get("_motor_mask")
    @property
    def thermo_master(self):
        return self.devices.get("_thermo_master")
    @property
    def thermo_0(self) -> aThermo:
        return self.devices.get("_thermo_0")
    @property
    def thermo_1(self) -> aThermo:
        return self.devices.get("_thermo_1")
    @property
    def door_safe(self) -> aDoorSafe:
        return self.devices.get("_door_safe")
    @property
    def sheath_sensor(self) -> aSheathSite:
        return self.devices.get("_sheath_sensor")
    @property
    def reagent_sensor(self) -> aReagentSite:
        return self.devices.get("_reagent_sensor")
    @property
    def fan(self) -> aFan:
        return self.devices.get("_fan")
    @property
    def led(self) -> aLed:
        return self.devices.get("_led")
    @property
    def uv(self) -> aUV:
        return self.devices.get("_uv")

    @property
    def is_safe(self) -> bool:
        return self.door_safe.is_on
    @property
    def has_sheath(self) -> bool:
        return self.sheath_sensor.is_on
    @property
    def has_reagent(self) -> bool:
        return self.reagent_sensor.is_on
    @property
    def status_acting(self)->str:
        #"extracting","sterilizing","waiting","paused"
        return self._status_acting
    @status_acting.setter
    def status_acting(self,value) -> str:
        if value in  ["extracting","sterilizing","waiting","paused"]:
            self._status_acting = value
        else:
            print("not proper status setting")

    def self_check(self):
        for device in self.devices:
            device.is_ok()
        return 
    def exit(self):
        self.end()
        # for device in self.devices:
        #     try:
        #         device.close()
        #     except Exception as e:
        #         print(e)
        # for thread in self.threads:
        #     try:
        #         thread.join(1)
        #     except Exception as e:
        #         print(e)
        pass

    def perform_step(self,partition:int,operation:Operation,step_idx:int):
        self.motor_stir.home_return()
        defaults= read_defaults()
        speed = operation.speed_mix
        if speed<=1: speed =1
        if speed>=3: speed =3

        self.motor_stir.set_points(operation.ul_volumn,
            defaults.get("motor_bottom").get("motor_stir"),
            *defaults.get("motor_speed")[speed-1])
        self.motor_mag.set_points(operation.ul_volumn,
            defaults.get("motor_bottom").get("motor_mag"))
        self.motor_disk.set_points(operation.ul_volumn,
            defaults.get("motor_bottom").get("motor_disk"))
        self.motor_mask.set_points(operation.ul_volumn,
            defaults.get("motor_bottom").get("motor_mask"))


        if int(step_idx) == 1:
            self.partition_ready(partition,1)
            self.first_touch()
        else:
            self.partition_ready(partition,operation.sec_wait)
        self.stir(operation.sec_mix)
        self.up(operation.sec_mag)

    def partition_ready(self,partition,sec_wait):
        self.motor_stir.home_return()
        self.motor_mag.bottom()
        self.motor_mask.bottom()
        self.motor_disk.grid(partition)
        self.motor_mask.home()
        self.motor_stir.liquid_wait(sec_wait)

    def first_touch(self):
        self.motor_stir.bottom_mag(3)
        
    def stir(self,sec_mix):
        if sec_mix>0:
            self.motor_stir.half_liquid()
            self.motor_mag.home()
            self.motor_stir.stir_mix(sec_mix)
            self.motor_stir.stop_mix()
            self.motor_stir.inner_liquid()
    def up(self,sec_mag):
        if sec_mag > 0:
            self.motor_stir.inner_liquid()
            self.motor_mag.bottom()
            self.motor_stir.bottom_mag(sec_mag)
        self.motor_stir.inner_liquid()

    def idle(self):
        self.motor_mask.home()
        self.motor_stir.home_return()
        self.motor_mag.home()
    def task_end(self):
        self.idle()
        # self.motor_mask.bottom()
        # self.motor_disk.grid(5)
        # self.motor_mask.home()
    def end(self):
        self.idle()
        self.motor_disk.grid(1)
        self.led.turn_off()

    def perform_moves(self,moves:List[Tuple[str]]):
        for move in moves:
            self.perform_move(move)

    def perform_move(self,move:Tuple[str]):
        steppers = {
            "z":self.motor_stir,
            "v":self.motor_mag,
            "x":self.motor_disk,
            "y":self.motor_mask,
            }
        stepper = steppers.get(move[0])
        action = getattr(stepper,move[1])
        action()

    def update(self):
        global info
        try:
            info.update({
                "disk_1_temperature":self.thermo_0.temperature,
                "disk_8_temperature":self.thermo_1.temperature,
                "disk":self.motor_disk._grid,
                "led_is_on":self.led.is_on,
                "fan_is_on":self.fan.is_on,
                "uv_is_on":self.uv.is_on,
                "door_at_spot":self.door_safe.is_on,
                "sheath_at_spot":self.has_sheath,
            })
        except Exception as e:
            print(e)
            # info.update({"disk":1})
            # raise e

class PauseTime():
    def __init__(self,pause_signal:Event,end:Event):
        self.pause_signal:Event = pause_signal
        self.end_signal:Event = end

    def sleep(self,seconds:int):
        seconds = int(seconds)
        self.pause_signal.clear()
        for i in range(seconds):
            if self.end_signal.is_set():
                break
            self.pause_signal.wait()
            time.sleep(1)

class MachinePause():
    def __init__(self,machine:MachineMain):
        self._machine = machine

    @Slot(int)
    def pause_pressed(self,checked:bool):
        if checked:
            Thread(target=self.pause).start()
        else:
            Thread(target=self.resume).start()
    def stop_pressed(self,pressed:int):
        Thread(target=self.stop).start()

    def pause(self):
        self._machine.motor_disk.pause()
        self._machine.motor_stir.pause()
    def resume(self):
        self._machine.motor_disk.resume()
        self._machine.motor_stir.resume()
    def stop(self):
        self._machine.motor_stir.stop()

        # self._machine.motor_disk.stop()

class Machine(MachineMain,MachinePause):
    def __init__(self,devices):
        super().__init__(devices)
        MachinePause.__init__(self,self)

class Machines:
    def connect_servers(self):
        _sers:Dict[str,aModbusServer] = {}
        for i in range(4):
            port = ["port_0","port_1","port_2","port_3"][i]
            try:
                _sers[f'server_{i}'] = servers.get_modbus_server(dm.get(port).get(SYS_NAME))
            except Exception as e:
                print(e)
                pass
        self.server_0:Union[aModbusServer,RtuMaster] = _sers["server_0"]
        self.server_1:Union[aModbusServer,RtuMaster] = _sers["server_1"]
        self.server_2:Union[aModbusServer,RtuMaster] = _sers["server_2"]
        self.server_3:Union[aModbusServer,RtuMaster] = _sers["server_3"]
        return _sers
    def close_servers(self):
        try:
            if not self.server_0 is None: self.server_0.close()
            if not self.server_1 is None: self.server_1.close()
            if not self.server_2 is None: self.server_2.close()
            if not self.server_3 is None: self.server_3.close()
        except Exception as e:
            print(e)

    def __del__(self):
        self.close_servers()
        
    def collect_devices(self):
        self.motor_stir = ls_steppers.get_stepper_ls(
            "motor_stir",self.server_1,dm.get("motor_stir"),
            defaults.get("motor_ppr").get("motor_stir"),
            defaults.get("motor_upr").get("motor_stir"),
            )
        self.motor_disk = wh_steppers.get_stepper_disk(
            "motor_disk",self.server_3,dm.get("motor_disk"),
            defaults.get("motor_ppr").get("motor_disk"),
            defaults.get("motor_upr").get("motor_disk"),
            )
        self.motor_mag = wh_steppers.get_stepper_mag(
            "motor_mag",self.server_3,dm.get("motor_mag"),
            defaults.get("motor_ppr").get("motor_mag"),
            defaults.get("motor_upr").get("motor_mag"),
            )
        self.motor_mask = wh_steppers.get_stepper_mask(
            "motor_mask",self.server_3,dm.get("motor_mask"),
            defaults.get("motor_ppr").get("motor_mask"),
            defaults.get("motor_upr").get("motor_mask"),
            )
        
        self.thermo_master = thermos.get_thermo_master(
            self.server_2,dm.get("thermos")
        )
        self.thermo_master.set_temperatrues((25,25,25,25))
        self.thermo_0 = thermos.get_thermo(
            "thermo_0",self.server_2,dm.get("thermos"),0)
        self.thermo_1 = thermos.get_thermo(
            "thermo_1",self.server_2,dm.get("thermos"),1)
        self.io = switches.get_ios(
            "ios",self.server_0,dm.get("ios"))
        self.door_safe = switches.get_sensor(
            self.io,dm.get("sensors").get("door_safe"))
        self.sheath_sensor = switches.get_sensor(
            self.io,dm.get("sensors").get("sheath_sensor"))
        self.reagent_sensor = switches.get_sensor(
            self.io,dm.get("sensors").get("reagent_sensor"))
        self.fan = switches.get_switch(
            self.io,dm.get("switches").get("fan"))
        self.led = switches.get_switch(
            self.io,dm.get("switches").get("led"))
        self.uv = switches.get_switch(
            self.io,dm.get("switches").get("uv"))

    def assemble_machine(self):
        self.motor_stir.set_motor_aware(self.motor_mask)
        self.motor_disk.set_motor_aware(self.motor_stir)
        devices = dict(
            _motor_stir=self.motor_stir,
            _motor_mag = self.motor_mag,
            _motor_disk = self.motor_disk,
            _motor_mask = self.motor_mask,
            _thermo_master = self.thermo_master,
            _thermo_0 = self.thermo_0,
            _thermo_1 = self.thermo_1,
            _door_safe = self.door_safe,
            _sheath_sensor = self.sheath_sensor,
            _reagent_sensor = self.reagent_sensor,
            _fan = self.fan,
            _led = self.led,
            _uv = self.uv
        )
        return Machine(devices)

    def get_machine(self):
        try:
            self.connect_servers()
            self.collect_devices()
            machine = self.assemble_machine()
            return machine 
        except Exception as e:
            print(e)
            # raise Exception("MachineInitError")
    
machines = Machines()

class TestMachine:
    def __init__(self):
        self.machine = machines.get_machine()
        self.machine.end()
    def test_light_open(self):
        self.machine.led.turn_on()
    def test_motors_return_home(self):
        print(
            self.machine.motor_stir.at_home,
            self.machine.motor_mag.at_home,
            self.machine.motor_disk.at_home,
            self.machine.motor_mask.at_home,
            )
        self.machine.motor_stir.home()
        self.machine.motor_mag.home()
        self.machine.motor_disk.home()
        self.machine.motor_mask.home()
        print(
            self.machine.motor_stir.at_home,
            self.machine.motor_mag.at_home,
            self.machine.motor_disk.at_home,
            self.machine.motor_mask.at_home,
            )
    def test_thermo(self):
        print(self.machine.thermo_0.temperature)
        print(self.machine.thermo_1.temperature)
        self.machine.thermo_0.set_temperatrue(50)
        self.machine.thermo_1.set_temperatrue(50)
        # time.sleep(5)
        print(self.machine.thermo_0.temperature)
        print(self.machine.thermo_1.temperature)
if __name__=="__main__":
    T = TestMachine()
    # T.test_light_open()
    # T.test_motors_return_home()
    T.test_thermo()