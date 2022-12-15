from prots import *


#TODO cancel this?
class Performer(aPerformer):
    def __init__(self,steps:List[list],machine:aMachine):
        self._steps = steps
        self._machine = machine
    @property
    def machine(self)->aMachine:
        return self._machine
    @property
    def steps(self)->List[list]:
        return self._steps
    