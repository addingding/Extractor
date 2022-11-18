import sys
import time
from threading import Event, Thread


class WithAble():
    def __enter__(self):
        if hasattr(self,'start'):
            self.start()
        return self
    def __exit__(self, type, value, trace):
        self.release()


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