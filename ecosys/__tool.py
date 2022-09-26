import sys,time
from threading import Thread,Event

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
        log = open('log.txt','a+',1,encoding="utf-8")
        sys.stdout = log
        print('--------------------------')
        print('\n',time.ctime())
    def release(self):
        sys.stdout = self.sysout_bak

logging = Logging()

class ResultThread(Thread):

    def __init__(self,func,args=()):
        super().__init__()
        self.func = func
        self.args = args
        self.finished = Event()
    def run(self):
        self.result = self.func(*self.args)
        self.finished.set()
    def get_result(self):
        try:
            self.finished.wait()
            return self.result
        except Exception:
            return None