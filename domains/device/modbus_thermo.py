from ecosys import *
from prots import *

from domains.device.modbus import *

class ThermoMaster(ModbusTerminal):
    def __init__(self, id: str, server: RtuServer, address: int):
        super().__init__(id, server, address)

    @property
    def temperatures(self) -> Tuple[float]:
        _tries =0
        t = None
        t = self.query(1,4)
        if t is None:
            t = (None,None,None,None)
        return t
    def set_temperatrues(self,ts:Tuple[int]) -> float:
        self.set_many_tuple(1,4,ts)
        return 

class Thermo(aThermo):
    def __init__(self,name,thermo_master,channel) -> None:
        super().__init__()
        self.name = name
        self.thermo_master:ThermoMaster = thermo_master
        self.channel = channel
    @property
    def temperature(self) -> float:
        return self.thermo_master.temperatures[self.channel]
    def set_temperatrue(self,t:float):
        ts = list(self.thermo_master.temperatures)
        ts[self.channel] = t
        self.thermo_master.set_many_tuple(1,4,tuple(ts))


class Thermos:
    _thermo_master = None
    def get_thermo_master(self,server,address):
        if self._thermo_master is None:
            self._thermo_master = ThermoMaster("thermo_master",server,address)
        return self._thermo_master

    def get_thermo(self,name,server,address,channel):
        _master = self.get_thermo_master(server,address)
        return Thermo(name,_master,channel)

thermos = Thermos()

class SelfTest():
    def test_thermo(self):
        logger.info("test thermo")

        server = servers.get_modbus_server("COM4" if sys.platform.startswith('win') else "/dev/ttySC0")
        thermo_master = thermos.get_thermo_master(server,3)
        logger.info(str(thermo_master.temperatures))
        thermo_master.set_temperatrues((50,50,50,50))
        # time.sleep(30)
        for i in range(4):
            thermo = thermos.get_thermo("thermo",server,3,i)
            logger.info(str(thermo.temperature))
        server.close()

def main():
    SelfTest().test_thermo()

if __name__ =="__main__":
    main()