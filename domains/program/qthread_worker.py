from prots import *
from ecosys import *


e_safe_collect = Event()
e_stop_collect = Event()



class TaskPerformer(Performer):
    signal_end = Signal(int)
    signal_updated = Signal(int)

class TempWorker(QThread):
    job_done = Signal(int)
    def work_for(self,task):
        self.task = task
    def run(self):
        self.task()
        self.job_done.emit(1)
