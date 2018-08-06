def grow(arr):
    x = 1
    for c in arr:
        x = x*c
    return x
    
    
"""
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)
"""


"""
from functools import reduce
from operator import mul

def grow(arr):
    return reduce(mul, arr, 1)
"""


"""
grow = lambda a: __import__("functools").reduce(lambda x,y: x*y, a)
"""
