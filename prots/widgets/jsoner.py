from ecosys import *

class Jsoner():
    def __init__(self,file:str):
        self.file = file
        self.data = dict()
        _dir = os.path.dirname(file)
        if not os.path.exists(_dir):
            os.mkdir(_dir)

        if not os.path.exists(file):
            self.save()
        else:
            self.load()

    def load(self):
        with open(self.file,'r') as f:
            self.data = json.load(f)
    def save(self):
        with open(self.file,'w') as f:
            json.dump(self.data,f)

    @property
    def last_idx(self)->int:
        _idx = 0
        if len(self.data)>0:
            _ids = [int(i) for i in self.data.keys()]
            _idx = max(_ids)
        return _idx

    def ins(self,idx:int):
        k = str(idx)
        v = self.data.get(k,None)
        if v is None:
            return
        else:
            return {k:v}
    def get_key(self,ins:dict):
        if len(ins)>0:
            return list(ins.keys())[0]
        else:
            return None

    def read(self,idx:int):
        return self.ins(idx)
    def create(self):
        new_idx = self.last_idx +1
        k = str(new_idx)
        self.data[k]= {}
        self.save()
        return self.ins(new_idx)
    def update(self,ins:dict):
        self.data.update(ins)
        self.save()
    def delete(self,idx:int,stp:int=None):
        k = str(idx)
        item = self.data.pop(k)
        if not stp is None:
            steps = item['steps']
            for i in range(len(steps)):
                if i == stp-1:
                    steps.pop(i)
            for i in range(len(steps)):
                steps[i][0] = i+1

            item.update({"steps":steps})
            self.data.update({k:item})
        self.save()
    def insert(self,idx:int,stp:int,ctx:tuple):
        k = str(idx)
        item = self.data.pop(k)
        steps:list = item['steps']
        steps.insert(stp-1,[stp,*ctx])
        for i in range(len(steps)):
            steps[i][0] = i+1
        item.update({"steps":steps})
        self.data.update({k:item})
        self.save()


class Objsoner():
    def __init__(self,model:object,jsoner:Jsoner):
        self.model = model
        self.jsoner = jsoner
    def obj(self,idx:int)->object:
        _ins = self.jsoner.ins(idx)
        if _ins is None:
            return
        else:
            return self.ins_to_obj(_ins)
    def get_obj_by_name(self,name:str,type_name:str='op_name'):
        assert name in self.obj_names(type_name)
        for obj in self.obj_all():
            _name = getattr(obj,type_name)
            if _name == name:
                return obj
            
    def obj_names(self,name:str='op_name'):
        return [getattr(self.obj(idx),name) for idx in self.obj_idxes()]
    def obj_idxes(self)->list:
        return list(self.jsoner.data.keys())
    def obj_all(self)->list:
        _idx_all = self.obj_idxes()
        _obj_all = []
        for idx in _idx_all:
            _obj_all.append(self.obj(idx))
        return _obj_all

    def ins_to_obj(self,ins:dict):
        _idx = int(self.jsoner.get_key(ins))
        _obj = self.model(idx=_idx)
        for key in self.model.keys:
            setattr(_obj,key,ins[str(_idx)].get(key))
        return _obj
    def obj_to_ins(self,obj:object):
        k = str(obj.idx)
        v = {}
        for key in self.model.keys:
            v.update({key:getattr(obj,key)})
        _ins = {k:v}
        return _ins

    def read(self,idx:int):
        return self.obj(idx)
    def create(self):
        _idx = self.jsoner.last_idx + 1
        _obj = self.model(idx=_idx)
        self.update(_obj)
        return _obj
    def copy(self,idx:int):
        _idx = self.jsoner.last_idx + 1
        _obj = self.model(idx=idx).copy()
        _obj.idx = _idx
        self.update(_obj)
        return _obj
    def update(self,obj:object):
        _ins = self.obj_to_ins(obj)
        self.jsoner.update(_ins)
    def delete(self,prg_idx:int,stp_idx:int=None):
        self.jsoner.delete(prg_idx,stp_idx)
    def insert(self,prg_idx:int,stp_idx:int):
        self.jsoner.insert(prg_idx,stp_idx,(1,"name",[0]*7))

