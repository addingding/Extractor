from prots import *
from domains.device.modbus import *


RelayStatus = namedtuple('RelayStatus',['ON','OFF'])
statuses = RelayStatus(0xFF00,0x0000)



class aSwitchRelay(ModbusTerminal):
    channels_in:int = 4
    channels_out:int = 4
    def __init__(self,id,server,address):
        super().__init__(id,server,address)
        assert self.channels_in <= 8
        assert self.channels_out <= 8
    def __del__(self):
        self.turn_off(1)
        self.turn_off(2)
        self.turn_off(3)
        self.turn_off(0)

    def _change_address(self):
        pass
    def _verify_address(self):
        pass

    def read_in(self):
        r = self.read_discs(self.channels_in)
        # answer_length = r[2]
        time.sleep(0.05)
        return r#[3:3+answer_length]
    
    def read_out(self):
        r = self.read_coils(self.channels_out)
        # answer_length = r[2]
        # time.sleep(0.05)
        return r#[3:3+answer_length]

    def point_switch_out(self,switch_index,status):
        r = None
        if status in statuses:
            time.sleep(0.05)
            r = self._execute(5,switch_index,output_value =status)
        return r#hex(r[4:6]) == status
    def turn_on(self,channel:int):
        self.point_switch_out(channel,0xFF00)
    def turn_off(self,channel:int):
        self.point_switch_out(channel,0x0000)


class Sensor(aSensor):
    def __init__(self,sw,channel:int):

        self.sw:aSwitchRelay=sw
        self.channel:int = channel
    @property
    def is_on(self):
        ret = None
        try:
            ret_ = self.sw.read_in()
            if ret_ is not None:
                ret = ret_[self.channel]
            return ret
        except Exception as e:
            print(self.__class__.__name__,e)
        return ret

class Switch(aSwitch):
    def __init__(self,sw,channel:int):
        self.sw:aSwitchRelay = sw
        self.channel:int = channel
        self.on = False
    def turn_on(self):
        self.sw.turn_on(self.channel)
        self.on = True
    def turn_off(self):
        self.sw.turn_off(self.channel)
        self.on = False
    @property
    def is_on(self):
        ret = None
        ret = None
        try:
            ret_ = self.sw.read_out()
            if ret_ is not None:
                ret = ret_[self.channel]
            return ret
        except Exception as e:
            print(self.__class__.__name__,e)
        return ret
    def switch(self):
        if self.on:
            self.turn_off()
        else:
            self.turn_on()

class Switches():
    def get_switch_server(self):
        import sys
        server = servers.get_modbus_server("COM4" if sys.platform.startswith('win') else "/dev/ttySC0")
        self.server = server
        return self.server

    def get_ios(self,name,server=None,address=1):
        if server is None:
            server = self.get_switch_server()
        ios= aSwitchRelay(name,server,address)
        return ios

    def get_sensor(self,ios:aSwitchRelay,channel:int):
        return Sensor(ios,channel)
    def get_switch(self,ios:aSwitchRelay,channel:int):
        return Switch(ios,channel)


switches = Switches()

def test_switch():
    sw = switches.get_ios("ios")
    print("in",sw.read_in())
    print("out",sw.read_out())
    sw.turn_on(0) # light
    sw.turn_on(1)   # fan

    sw.turn_off(2)
    time.sleep(0.5)
    sw.turn_on(2)

    print("in",sw.read_in())
    print("out",sw.read_out())

    time.sleep(3)
    sw.turn_off(0)
    sw.turn_off(1)
    sw.turn_off(2)
    print("out",sw.read_out())

def test_led():
    sw = switches.get_ios("ios")
    led = switches.get_switch(sw,0)
    led.turn_on()
    step_stop = switches.get_switch(sw,3)
    step_stop.turn_on()
    
    door_safe = switches.get_sensor(sw,0)
    reag_safe = switches.get_sensor(sw,1)
    print(door_safe.is_on,reag_safe.is_on)

    time.sleep(3)
    for i in range(5):
        led.switch()
        time.sleep(1)
        led.switch()
        time.sleep(1)


def main():
    # test_switch()
    test_led()
if __name__=="__main__":
    main()