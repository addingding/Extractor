from ecosys.__log import logger


def get_attrs(aClass):
    def is_callable_attr(a:str):
        return callable(aClass.__dict__.get(a)) and\
            (not a.startswith("__"))
    def is_property_attr(a:str):
        return (not callable(aClass.__dict__.get(a))) and\
            (not a.startswith("__"))
    attrs = dir(aClass)
    c = list(filter(is_callable_attr,attrs))
    p = list(filter(is_property_attr,attrs))
    return c,p

class Simulator():
    def __init__(self,aClass) -> None:
        self._sim = aClass
    def __getattribute__(self, __name: str):
        _sim = super().__getattribute__("_sim")
        try:
            attr = getattr(_sim,__name)
        except AttributeError:
            print("Lack Attr",_sim,__name)
            return print

        _c,_p = get_attrs(_sim)
        def printf(*args,n=None,**kw):
            _cls = _sim.__name__
            print(f"{_cls}.{__name}({n})")
            return f"{_cls}.{__name}({n})"
        try:
            if __name in _c:
                return printf
            elif __name in _p:
                #property
                if hasattr(attr,"fget"): 
                    _attr = getattr(attr,'fget')
                    annotations = _attr.__annotations__
                
                    # has annotation
                    if "return" in annotations.keys():  
                        print(f"->{_sim.__name__}.{__name}")
                        _type = annotations.get("return")
                        if _type in [str,int,float,bool,list,dict,tuple,set]:
                            return f"->{_type.__name__}"
                        else:
                            return Simulator(_type)
                    # no annotation
                    else:                               
                        # print(__name,"cited")
                        pass
                # attribute
                else:                   
                    # print(__name,"attr cited")
                    pass
            else:
                print(":::Simulator NotFind:::")
                return printf
        except Exception as e:
            logger.error("error")
            return printf
aSim = Simulator