import json
from typing import Any


class Config():
    def __init__(self,config_file) -> None:
        self.__dict__["config_file"] = config_file
        with open(config_file,"r",encoding="utf-8") as f:
            _configs = json.load(f)
        self.__dict__.update(_configs)

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