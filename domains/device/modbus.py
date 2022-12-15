# -*- coding: utf_8 -*-
from ecosys import *

import serial
import modbus_tk
from modbus_tk import modbus_rtu
from modbus_tk.modbus_rtu import RtuMaster, RtuServer


modbus_interval = 0.001
def binstring(n,ln)->str:
    return f"{n:0{ln}b}"
def bin_get(n:int,idx:int)->bool: #0-15/31
    r = n >> (idx)
    _r = r -((r>>1)<<1)
    return _r

def serial_ports():

    if sys.platform.startswith('win'):
        available_ports = ['COM%s' % (i + 1) for i in range(16)]
        logger.info("Windows platform")
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal"/dev/tty"
        available_ports = glob.glob('/dev/tty[A-Za-z]*')
        logger.info("Linux platform")
    elif sys.platform.startswith('darwin'):
        available_ports = glob.glob('/dev/tty.*')
        logger.info("Darwin kernal")
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in available_ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

available_ports = serial_ports()
logger.info(f"working serial_ports:{available_ports}",)

# @dataclass
# class Message():
#     Address:bytes     #1 Byte
#     Function:bytes    #1 Byte
#     Data:bytes        #n Bytes
#     Check:bytes       #2 Bytes


class Servers():
    _servers = {}
    def get_server(self,port,timeout=1.0,server_type:str="modbus"):
        return self._get_server(port,timeout,server_type)
    def get_modbus_server(self,port,timeout=1.0):
        return self._get_server(port,timeout,"modbus")
    def get_serial_server(self,port,timeout=1.0):
        return self._get_server(port,timeout,"serial")

    def _get_server(self,port,timeout=1.0,server_type:str="modbus"):
        if port not in available_ports:
            return
        if port in self._servers:
            return self._servers.get(port)
        else:
            return self._create_server(port,timeout,server_type)

    def _create_server(self, port, timeout,server_type):
        server = None
        if server_type == "modbus":
            server = self._create_a_modbus(port,timeout)
            time.sleep(0.1)
        else:
            server = self._create_a_serial(port,timeout)
            time.sleep(0.1)
        server.lock = Lock()
        server.open()
        self._servers[port]= server
        return server
    def _create_a_modbus(self, port, timeout):
        _modbus_server = RtuMaster(self._get_a_serial_device(port))
        _modbus_server.set_timeout(timeout)
        _modbus_server.set_verbose(True)
        return _modbus_server
    def _create_a_serial(self,port,timeout=0.05):
        _serial = self._get_a_serial_device(port,timeout)
        return _serial

    def _get_a_serial_device(self,port,timeout=1):
        ser = None
        try:
            ser = serial.Serial(
                port=port,
                baudrate = 115200, 
                bytesize=8, 
                parity='N', 
                stopbits=1, 
                xonxoff=0)
            ser.timeout = timeout
        except Exception as e:
            logger.error(f"{self.__class__.__name__},{e}")
        return ser

    def __del__(self):
        for ser in self._servers:
            try:
                self._servers.get(ser).close()
            except Exception as e:
                logger.error(f"{self.__class__.__name__},{e}")
    

servers = Servers()

class FakeServers():
    class FakeModbusServer():
        def __init__(self):
            self.lock = Lock()
        def open(self):
            return True
        def close(self):
            return True
        def execute(self,*args,**kws):
            if args[0]==10 and args[1]==3 and args[3]==1:
                if args[2] == 0x1001+1:
                    return [200]
                elif args[2] == 0x1001+0:
                    return [600]
            new_args = [str(i) for i in args]
            return str("".join(new_args))

    def get_modbus_server(self,port,timeout=1.0):
        return FakeServers.FakeModbusServer()
fake_servers = FakeServers()

def oxstring(n,ln):
    return f"{n:0{ln}X}"
def register_data_get(registers:int,data:int)->List[int]:
    ls_data = []
    s_data = oxstring(data,registers*4)
    for i in range(registers):
        _data = s_data[i*2*2:(i+1)*2*2]
        ls_data.append(int(_data,16))
    return tuple(ls_data)


class ModbusTerminal():
    def __init__(self,id:str,server:RtuServer,address:int):
        self.id = id
        self.server = server
        self.address = address
        time.sleep(0.5)

    @property
    def is_working(self):
        try:
            ret = self._execute(3,1,1)
            if ret is not None:
                return True
        except Exception as e:
            logger.error(f"{self.__class__.__name__},{e}")
            return

    def _execute(self,function_code,data_start,data_quantity=1,output_value=None):
        with self.server.lock:
            try_times = 1
            for i in range(try_times):
                try:
                    return self.server.execute(self.address,function_code,data_start,data_quantity,output_value=output_value)
                except Exception as e:
                    logger.error(f"modbus with lock: {self.address},{function_code},{hex(data_start)},{self.__class__.__name__},{e}")
                    # logger.info("retry.")
                    # time.sleep(0.1)
        # logger.info(f"failed to excute.")
        # logger.error(f"modbus with lock: {self.address},{function_code},{hex(data_start)},{self.__class__.__name__},{e}")
                
    def _execute_(self,function_code,data_start,output_value=None):
        try_times = 1    
        for i in range(try_times):
            try:
                return self.server.execute(self.address,function_code,data_start,output_value=output_value)
            except Exception as e:
                logger.error(f"modbus {self.address},{function_code},{hex(data_start)},{self.__class__.__name__},{e}")
                # logger.info("retry")
                # time.sleep(0.1)
        # logger.info(f"failed to excute.")
        # logger.error(f"modbus {self.address},{function_code},{hex(data_start)},{self.__class__.__name__},{e}")

    def read_coils(self,data_quantity):#out
        return self._execute(1,0,4)
    def read_discs(self,data_quantity):#in
        return self._execute(2,0,4)

    def query(self,data_start,data_quantity=1):
        return self._execute(3,data_start,data_quantity)
    def set_single(self,data_start,output_value):
        return self._execute_(6,data_start,output_value=output_value)
    def set_many_tuple(self,data_start,quantity:int,output_value:Tuple[int]):
        return self._execute(0x10,data_start,output_value = output_value)
   
    def set_many(self,data_start:int,quantity:int,output_value:int):
        _value = register_data_get(quantity,output_value)
        return self._execute(0x10,data_start,output_value=_value)
        
    def _change_address(self):
        raise  NotImplemented
    def reset_address(self):
        self._change_address(self.address)

    def _verify_address(self):
        raise NotImplemented





class SelfTest():
    # def test_cmd(self):
    #     cmd = Command(1, modbus_tk.defines.READ_HOLDING_REGISTERS, 2700, 43)
    #     print(*cmd.__repr__())
    def test_serial_ports(self):
        print("test_serial_ports")
        print(f"{serial_ports()}")

    def test_open_close(self):
        server = servers.get_modbus_server("COM4" if sys.platform.startswith('win') else "/dev/ttySC1")
        server.close()
    def test_get_device_list(self):
        # server = servers.get_modbus_server("COM4" if sys.platform.startswith('win') else "/dev/ttySC0")
        server = servers.get_modbus_server("COM4" if sys.platform.startswith('win') else "/dev/ttySC1")
        print("server:",servers._servers)

        if server is None: 
            print("no real server to use")
            return
        server.set_timeout(0.1)

        _devices = []

        for i in range(32):
            try:
                ret = server.execute(i,3,1,1)
                time.sleep(0.1)
                _devices.append(i)
            except Exception as e:
                # print(i,self.__class__.__name__,e)
                print('check',i,end='\r')
                pass
        print('\n',_devices)
        server.set_timeout(1)
        server.close()



def main():
    T = SelfTest()
    # T.test_cmd()
    # T.test_serial_ports()
    # T.test_open_close()
    T.test_get_device_list()

if __name__ == "__main__":
    main()