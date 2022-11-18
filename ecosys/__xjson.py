import json

import numpy as np

from .__pies import *


class ConfigDict():
    def __init__(self,dic:dict):
        self.__dict__.update(dic)

class Config():
    def __init__(self,config_file) -> None:
        if os.path.exists(config_file):
            self.__dict__["config_file"] = config_file
            with open(config_file,"r",encoding="utf-8") as f:
                _configs = json.load(f)
            self.__dict__.update(_configs)
        else:
            raise Exception("NotExist")
class Configure(Config):
    def __init__(self, config_file, hook=None) -> None:
        super().__init__(config_file)
        self.__dict__["hook"] = hook
    def __setattr__(self, name: str, value: Any) -> None:
        self.__dict__.update({name:value})
        if not name.startswith("__"):
            with open(self.config_file,"w",encoding="utf-8") as f:
                json.dump(self.__distill(self.__dict__),f)
        if self.hook is not None and callable(self.hook):
            self.hook(name,value)
    def __distill(self,dict_:dict):
        dic =dict_.copy()
        del dic["config_file"]
        del dic["hook"]
        return dic

class Records:
    def __init__(self,records_file):
        self.__file = records_file
        self.__records:dict = self.__get_records()
    @property
    def records(self):
        return self.__records
    def __get_records(self):
        with open(self.__file,"r",encoding="utf-8") as f:
            _records = json.load(f)
        return _records

    def get_record(self,key):
        return self.__records.get(key)
    def put_record(self,key,value):
        self.__records.update({key:value})
        with open(self.__file,"w",encoding="utf-8") as f:
            json.dump(self.__records,f)
    def update_all(self,dict_):
        self.__records.update(dict_)
        with open(self.__file,"w",encoding="utf-8") as f:
            json.dump(self.__records,f)

# ========================================================================================
# ========================================================================================
# ========================================================================================


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self,object_hook=self.dict2object)
        
    def dict2object(self,obj):
        #convert dict to object
        if '__class__' in obj:
            class_name = obj.pop('__class__')
            print("class_name:",class_name)
            module_name = obj.pop('__module__')
            print("module_name:",module_name)
            module = importlib.import_module(module_name)
            class_ = getattr(module,class_name)
            print(class_)
            args = dict((key, value) for key, value in obj.items()) #get args
            print(args)
            inst = class_(**args) #create new instance
        else:
            inst = obj
        return inst        



# def test_json_serial():
#     test_words = dict(
#         a=[Vec(1,2)],
#         b=[Box(1.2,1.3,2,5)]
#     )
#     with open("test.json","w") as f:
#         json.dump(test_words,f,cls=MyEncoder)

#     with open("test.json","r") as f:
#         k = json.load(f,cls=MyDecoder)
#         print(k['a'])
#         print(k['b'])
