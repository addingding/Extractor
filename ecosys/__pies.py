import cProfile
import datetime
import glob
import importlib
import json
import math
import os
import random
import shutil
import sys
import time
from abc import *
from collections import *
from dataclasses import *
from functools import *
from itertools import *
from typing import *  # List,Dict,Any,Union,Optional,Tuple

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



