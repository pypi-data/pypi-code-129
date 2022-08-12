
import numpy as np
import torch
import  sys
import inspect
import prettytable as pt
# from prettytable import *

__all__ = ['gprint','mprint',]

class GY_DEFINE_COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW_BG = '\033[1;35;43m'

def gprint(_args : None, 
        show_table: bool = True,
        show_value: bool = False,
        segfix : str ="=====>",
        nested : bool = False
        ) -> None:
    '''
    TODO 
    * 1. recursive print !!! list --> dict -> ...
    * 2. table show
    '''
    assert _args is not None, f"please promise gyprint.print_shape Tensor is not None, {print_shape.__annotations__}" 
    assert type(segfix) is str, f"please promise gyprint.print_shape segfix is str, {print_shape.__annotations__}"
    def __retrieve_name(__var) -> None:
        assert __var is not None, "please promise __var is not None"
        if nested:
            callers_local_vars = inspect.currentframe().f_back.f_back.f_back.f_locals.items()
        else:
            callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is __var]
    __tensor_name = __retrieve_name(_args)[0]
    if type(_args) == torch.Tensor or type(_args) == np.ndarray:
        print(GY_DEFINE_COLORS.YELLOW_BG+f'{__tensor_name} {segfix} {type(_args)} {segfix} {_args.shape}'+GY_DEFINE_COLORS.ENDC)
        return
    
    # tb.set_style(RANDOM) # PLAIN_COLUMNS,MSWORD_FRIENDLY
    def __print_tensor_shape(_tensor,keys = None,colors = None, null_value = False):
        if null_value:
            if not show_table:
                print(f'你的这个{type(_args)}里面并非tensor或numpy值,它的具体信息是 {keys}:{type(_tensor)}')
            else:
                tb.add_row([__tensor_name,keys,type(_tensor),"No Size!"])
            return
        if keys is not None:
            if not show_table:
                print(f'{__tensor_name}, keys: {keys}, value{segfix} {type(_tensor)} {segfix} {_tensor.shape}')
            else:
                tb.add_row([__tensor_name,keys,type(_tensor),_tensor.shape])
        
    if isinstance(_args,(list,tuple)):
        tb = pt.PrettyTable()
        tb.field_names = [f"{type(_args)}:{len(_args)}", "index/keys()", "value type", "Size Info"]
        print(GY_DEFINE_COLORS.OKGREEN,'#'*15,f'{__tensor_name} is {type(_args)}, length is {len(_args)}','#'*15,GY_DEFINE_COLORS.ENDC)\
            if not show_table else None
        # _args = _args if type(_args) == list else list(_args)
        for index, item in enumerate(_args):
            if isinstance(item, (torch.Tensor,np.ndarray)):
                __print_tensor_shape(item, keys=index)
            else:
                __print_tensor_shape(item, keys=index,null_value=True)
        print(GY_DEFINE_COLORS.OKGREEN,end='')
        print(tb) if show_table else None
        print(GY_DEFINE_COLORS.ENDC,end='')
    elif isinstance(_args,dict):
        # then print key:value, method type, else no implementation
        tb = pt.PrettyTable()
        tb.field_names = [f"{type(_args)}:{len(_args)}", "index/keys()", "value type", "Size Info"]
        print(GY_DEFINE_COLORS.OKBLUE,'#'*15,f'{__tensor_name} is {type(_args)}, length is {len(_args)}','#'*15,GY_DEFINE_COLORS.ENDC)\
            if not show_table else None
        for keys, value in _args.items():
            # assert isinstance(value,(torch.Tensor,np.ndarray)), f"please promise the value of {__tensor_name} is torch.Tensor or numpy"
            if isinstance(value,(torch.Tensor,np.ndarray)):
                __print_tensor_shape(value,keys=keys)
            else:
                __print_tensor_shape(value,keys=keys,null_value=True)
        print(GY_DEFINE_COLORS.OKBLUE,end='')
        print(tb)  if show_table else None
        print(GY_DEFINE_COLORS.ENDC,end='')
    else:
        print(f"===========你要打印的这个变量{__tensor_name},该类型是{type(_args)}目前还不支持哦,那没办法的呀，所以我要报错==========")
        raise NotImplementedError
    print(f"{__tensor_name} {segfix} ",_args) if show_value else None
        
def mprint(*args,
                    )->None:
    for item in args:
        gprint(item,nested=True)
