from ecosys import *
from prots import *

# idx:int
# ins:dict = {k:v}
# obj:object = Model(idx=idx,**kwargs)
# hasattr(Model,"keys")

operations_file = os.path.join(BASE_DIR,"app","data","operations.json")
programs_file = os.path.join(BASE_DIR,"app","data","programs.json")
tasks_file = os.path.join(BASE_DIR,"app","data","tasks.json")

@dataclass
class Move(aMove):

    def get_point(self):
        ...

class MoveGroup():
    def __init__(self,name:str) -> None:
        self.name = name
        self.moves = []
    def add_move(self,move:aMove):
        self.moves.append(move)


@dataclass
class Operation(aOperation):
    keys = [
        "op_name",
        "sec_wait","sec_mix","sec_mag",
        "ul_volumn","speed_mix","temperature"]
    sec_wait:int= 0  # 0-600
    sec_mix:int = 0  # 0-1800
    sec_mag:int = 0 # 0-300
    ul_volumn:int = 0 # 50-1000
    speed_mix:int = 0 # 1-3
    temperature:int = 0 #30-80


@dataclass
class Step(aStep):
    def __str__(self):
        return list(astuple(self))
    def __post_init__(self):
        self._operation:Operation = self.get_operation()
    @property
    def operation(self)->aOperation:
        return self._operation

    def get_operation(self):
        with open(operations_file,'r') as f:
            op_dict = json.load(f)
        _operation = Operation(idx=self.operation_idx)
        _operation.__dict__.update(op_dict.get(self.operation_idx))
        return _operation

class Program(aProgram):
    keys = ["pg_name","steps"]
    def add_step(self,step:Step):
        self.steps.append(list(astuple(step)))

    def __str__(self):
        return list((self.idx,self.pg_name))

class Task():
    keys=["created_time","program","status","current_pos"]
    def __init__(self,idx:int):
        self.idx:int = idx
        self.created_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.status:int = 0 #create,assigned,working,paused,finished,canceled
        self.current_pos:list = [0,0,0] #partition,motor_pos,time_left
        self.program:Program = None
    def assign_program(self,program):
        self.program = program
        self.status = 1




class OperationJsoner(Singleton,Jsoner):
    pass
class ProgramJsoner(Singleton,Jsoner):
    pass
class TaskJsoner(Singleton,Jsoner):
    pass
class Programers():
    def operation_handler(self):
        return Objsoner(Operation,OperationJsoner(operations_file))
    def program_handler(self):
        return Objsoner(Program,ProgramJsoner(programs_file))
    def task_handler(self):
        return Objsoner(Task,TaskJsoner(tasks_file))

programers = Programers()





class TestOperations():
    def test_operation(self):
        operation = programers.operation_handler()
        operation.delete(4)
        new_obj = operation.create()
        new_obj.op_name = "with_mixture"
        new_obj.sec_mag =99
        operation.update(new_obj)
        print(operation.obj_all())
    def test_program(self):
        program = programers.program_handler()
        # program.delete(4)
        new_obj = program.create()
        new_obj.pg_name = "20220101"
        new_obj.steps = [[1,1,"2"],[2,2,"5"]]
        program.update(new_obj)
        print(program.obj_all())
    def test_task(self):
        task = programers.task_handler()
        # task.delete(4)
        new_obj = task.create()
        print(task.obj_all())


if __name__ == "__main__":
    t = TestOperations()
    # t.test_operation()
    t.test_program()
    # t.test_task()