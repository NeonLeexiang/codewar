def digits(num):
    return_list = []
    num = list(map(int,str(num)))
    for i in range(len(num)):
        for j in range(1,len(num)-i):
            return_list.append(num[i]+num[i+j])
    return return_list
    
    
"""
from itertools import combinations

def digits(num):
    return list(map(sum, combinations(map(int,str(num)),2)))
"""


"""
def digits(num):
    parse = lambda s: [int(s[0]) + int(x) for x in s[1:]] + (digits(s[1:]) if len(s) > 2 else [])
    return parse(str(num))
"""


"""
digits=lambda n:list(map(sum,__import__("itertools").combinations(map(int,str(n)),2)))
"""


"""
def digits(num):
    return [int(x) + int(y) for i, x in enumerate(str(num)[:-1]) for y in str(num)[i + 1:]]
"""
