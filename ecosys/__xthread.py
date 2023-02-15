import asyncio
from queue import *
from threading import *

from ecosys.__log import logger
from ecosys.__pies import *


def start_source_threading(obj:object,thread_name:str,target_obj:object,args:tuple) -> None:
    """ start a stand_alone threading with some source occupation """
    if hasattr(obj,thread_name):
        _m = getattr(obj,thread_name)
        if hasattr(_m,"join"):# and (not _m.is_alive()):
            _m.join(0.01)
            del _m
    setattr(obj,thread_name,None)
    _m = getattr(obj,thread_name)
    _m = Thread(target=target_obj,args=args)
    _m.start()

class LatestQueue():
    def __init__(self,_maxsize):
        self.queue = LifoQueue(_maxsize)
    def put(self,_item):
        if self.queue.full():
            self._clear()
        try:
            self.queue.put_nowait(_item)
        except Exception as e:
            logger.error("error")

    def get(self):
        data = self.queue.get()
        self._clear()
        return data

    def qsize(self):
        return self.queue.qsize()

    def _clear(self):
        try:
            while True:
                if not self.queue.empty():
                    _ = self.queue.get_nowait()
                else:
                    break
        except Exception as e:
            logger.error("error")
            pass

class LineWorker():
    def __init__(self,job,*args,**kwargs):
        self.dismiss = Event()
        self.go = Event()
        self.thread = Thread(target=self.work,daemon=True)
        self.job = job
        self.args = args
        self.kwargs = kwargs
        self.thread.start()

    def start_work(self):
        self.go.set()
    def work(self):
        while not self.dismiss.is_set():
            self.go.wait()
            self.job(*self.args,**self.kwargs)
            time.sleep(0.001)
    
    def pause(self):
        self.go.clear()
    def resume(self):
        self.go.set()

    def pause_switch(self):
        if self.go.is_set():
            self.go.clear()
        else:
            self.go.set()

    def stop(self):
        self.dismiss.set()
    def exit(self):
        self.stop()

class JobWorker():
    def __init__(self,job,*args,**kwargs):
        self.finished = Event()
        self.dismiss = Event()
        self.thread = Thread(target=self.work,daemon=False)
        self.job = job
        self.args = args
        self.kwargs = kwargs
        self.working = Event()

    def work(self):
        while not self.dismiss.is_set() or not self.finished.is_set():
            finished = self.job(*self.args,**self.kwargs)
            if finished:
                self.finished.set()
            time.sleep(0.001)

    def start_work(self):
        self.thread.start()
        self.working.set()

    def stop(self,timeout:float=1.0):
        self.dismiss.set()
        self.finished.wait(timeout)
        if hasattr(self,"thread") and self.thread.is_alive():
            self.thread.join(1)
        self.working.clear()
    def exit(self):
        self.stop()
    def hard_exit(self):
        self.finished.set()
        self.stop()




# ===========================================================================
# ===========================================================================
# ===========================================================================
# ===========================================================================
# ===========================================================================
def utest_job_worker():
    job_list = list(range(20))
    i = 0
    def job():
        nonlocal i
        i +=1
        print(i)
        time.sleep(0.1)
        if i == 19:
            return True
    _worker = JobWorker(job)
    _worker.start_work()
    time.sleep(1)
    print("safe_stop!!!!")
    _worker.exit()
def utest_job_worker_hard():
    job_list = list(range(20))
    i = 0
    def job():
        nonlocal i
        i +=1
        print(i)
        time.sleep(0.1)
        if i == 19:
            return True
    _worker = JobWorker(job)
    _worker.start_work()
    time.sleep(1)
    print("hard_stop!!!!")
    _worker.hard_exit()

def utest_flow_worker():
    i = 0
    def job():
        nonlocal i
        print("i'm working...",i)
        i += 1
        time.sleep(0.2)
    _worker = LineWorker(job)
    
    _worker.start_work()
    time.sleep(2)
    
    print("have_a_rest")
    _worker.pause()
    for k in range(2):
        print("rest_1s")
        time.sleep(1)

    print("continue_work")
    _worker.resume()
    time.sleep(2)
    
    print("dismiss!!!!")
    _worker.stop()


if __name__=="__main__":
    utest_job_worker()
    utest_job_worker_hard()
    utest_flow_worker()
    pass