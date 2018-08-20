def find_it(seq):
    odd = 0
    for i in seq:
        odd ^= i
    return odd


"""
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""


"""
import operator

def find_it(xs):
    return reduce(operator.xor, xs)
"""


"""
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
"""


"""
find_it = lambda seq: [x for x in seq if seq.count(x) % 2 != 0][0]
"""
