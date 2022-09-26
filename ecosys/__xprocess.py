from multiprocessing import cpu_count,freeze_support,Pool
# from pathos.helpers import cpu_count, freeze_support, ProcessPool as Pool
freeze_support()
import multiprocessing.dummy
# from multiprocessing.dummy import DummyProcess
from multiprocessing.dummy.connection import Pipe