import datetime
import logging
import sys
from logging import handlers


class WithAble():
    def __enter__(self):
        if hasattr(self,'start'):
            self.start()
        return self
    def __exit__(self, type, value, trace):
        self.release()

class Logging(WithAble):
    sysout_bak = sys.stdout
    def start(self):
        import time
        log = open('log.txt','a+',1)
        sys.stdout = log
        print('--------------------------')
        print('\n',time.ctime())
    def release(self):
        sys.stdout = self.sysout_bak

   
class MyLogger():
    def __init__(self,name,console:bool=True,backup:bool=True,error:bool=True):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        if console:
            self.start_console_logger()
        if backup:
            self.start_backup_logger()
        if error:
            self.start_error_logger()

    def __getattr__(self,attr:str):
        return getattr(self.logger,attr)

    def start_console_logger(self):
        rf_handler = logging.StreamHandler(sys.stderr)#默认是sys.stderr
        rf_handler.setLevel(logging.DEBUG) 
        rf_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s -%(filename)s:%(lineno)d"))
        self.logger.addHandler(rf_handler)

    def start_backup_logger(self,filename:str="back.log"):
        _handler = handlers.TimedRotatingFileHandler(
                filename,when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
        _handler.setLevel(logging.DEBUG)
        _handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(message)s",
                datefmt='%y-%m-%d %H:%M:%S'))
        self.logger.addHandler(_handler)



    def start_error_logger(self,filename:str="error.log"):
        _handler = logging.FileHandler(filename)
        _handler.setLevel(logging.ERROR)
        _handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s %(message)s -%(filename)s:%(lineno)d ",
                datefmt='%y-%m-%d %H:%M:%S'))
        self.logger.addHandler(_handler)

class Loggers():
    def logger(self,name,console:bool=1,backup=1,error=1):
        return MyLogger(name,console,backup,error)

loggers = Loggers()
logger:logging = loggers.logger("ProjectLogger",1,1,1)