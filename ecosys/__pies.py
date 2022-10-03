from __future__ import annotations
import sys
import os
import time
import datetime
import math
import random
import glob
import shutil
import json

import importlib
import cProfile

from abc import *
from functools import *
from dataclasses import *
from collections import *
from typing import * #List,Dict,Any,Union,Optional,Tuple
from itertools import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGUAGES = [0]

def get_sys_name():
    if sys.platform.startswith('win'):
        return "Windows"
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        return "Linux"
    elif sys.platform.startswith('darwin'):
        return "Darwin"
    else:
        raise EnvironmentError('Unsupported platform')
SYS_NAME = get_sys_name()


def time_serial():
    t = datetime.datetime.now()
    s = t.strftime("%y%m%d_%H%M%S")
    return s

def newline():
    print("\n")

def get_methods(cls:object):
    attrs = dir(cls)
    def _is_method(attr):
        return callable(getattr(cls,attr)) and (not attr.startswith("_"))
    return list(filter(_is_method,attrs))

def get_three_int_str(n:int) -> str:
    assert 0 <= n <= 999
    return str(1000+n)[-3:]

def mytry(f,*args,**kwargs):
    try:
        f(*args,**kwargs)
    except Exception as e:
        print(e)

def func_time(f):
    """
    简单记录执行时间
    :param f:
    :return:
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__, 'took', end - start, 'seconds')
        return result

    return wrapper


def func_cprofile(f):
    """
    内建分析器
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = f(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats(sort='time')
    return wrapper


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

def dict_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst = Dict()
    for k,v in dictObj.items():
        inst[k] = dict_object(v)
    return inst


def convert_path(path: str) -> str:
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)


def cost_timer(function):
    '''
    装饰器实现函数计时
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print(f'{function.__name__} spent { round(t1 - t0,4)}s')
        return result
    return function_timer
def show_name(function):
    """ 测试的函数自动打印自己的函数名 """
    @wraps(function)
    def test_func(*args,**kw):
        print (f'\n......{function.__name__}......')
        function(*args, **kw)
        print("...... end of test ......\n")
        return function
    return test_func

def attach(text):
    def decorator(function):
        print(text)
        @wraps(function)
        def wrapper(*args,**kw):
            return function(*args,**kw)
        return wrapper
    return decorator


class WithAble():
    def __enter__(self):
        if hasattr(self,'start'):
            self.start()
        return self
    def __exit__(self, type, value, trace):
        self.release()

class Logging(WithAble):
    sysout_bak = sys.stdout
    def start(self):
        import time
        log = open('log.txt','a+',1)
        sys.stdout = log
        print('--------------------------')
        print('\n',time.ctime())
    def release(self):
        sys.stdout = self.sysout_bak

class RollbackAble:
    def __init__(self,charge_board:list):
        self.rollback_able = True
        self.charge_board= charge_board
        self._buffer = {}
        self._changes = {}
        self._buffer_status()
    def _buffer_status(self):
        for key,value in self.__dict__.items():
            if key in self.charge_board: 
                self._buffer[key]=value
    
    def reload(self):
        self.__dict__.update(self._buffer)
    
    def cancel_changes(self):
        self.reload()
    def redo_change(self):
        self.__dict__.update(self._changes)

    def _buffer_change(self,**kws):
        self._buffer.update(self._changes)
        self._changes = kws

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
        attr = getattr(_sim,__name)

        _c,_p = get_attrs(_sim)
        def printf():
            _cls = _sim.__name__
            print(f"{_cls}.{__name}()")
            return f"{_cls}.{__name}()"
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
                    print(__name,"cited1")
            # attribute
            else:                   
                print(__name,"attr cited")
        else:
            print(":::Simulator NotFind:::")
            return printf
aSim = Simulator