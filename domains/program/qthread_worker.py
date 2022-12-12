from ecosys import *
from prots import *

e_safe_collect = Event()
e_stop_collect = Event()



class TaskPerformer(Performer):
    signal_end = Signal(int)
    signal_updated = Signal(int)

class QWorker(QThread):
    job_done = Signal(int)
    job_update = Signal(int)
    def work_for(self,task):
        self.task = task
    def run(self):
        ret:int = self.task()
        if ret is None:
            ret = 0
        self.job_done.emit(int(ret))

