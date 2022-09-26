from ecosys import *

@dataclass
class aUser:
    sid:str
    login_code:str
    password:str
    name:str
    signature:str
    role:str
@dataclass
class aConfigor(aUser):
    role:str = "configor"
    code_length = 4
class aOperator(aUser):
    role:str = "operator"
    code_length = 3
class aInspector(aUser):
    role:str = "checker"
    code_length = 4