"""
符号式编程方式工具

"""
import torch
import torch.nn as nn

def transjit(net):
    return torch.jit.script(net)

# ppkl = """
# import torch
# def add(a, b):
#     return a + b
#
# def fancy_func(a, b, c, d):
#     e = add(a, b)
#     f = add(c, d)
#     g = add(e, f)
#     return g
# print(fancy_func(1, 2, 12, 4))
# """
# z = compile(ppkl,'','exec')
# exec(z)
#


