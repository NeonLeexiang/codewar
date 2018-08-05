def solution(a, b) :
    translation = {"kg":1,"g":0.001,"mg":0.000001,"μg":0.000000001,"lb": 0.453592,
                   "m":1,"cm":0.01,"mm":0.001,"μm":0.000001,"ft": 0.3048}
    return 6.67e-11*(a[0]*translation[b[0]]*a[1]*translation[b[1]])/((a[2]*translation[b[2]])**2)
    

"""
from itertools import starmap

G = 6.67e-11
CONVERSIONS = {'cm': 1e-2, 'mm': 1e-3, 'μm': 1e-6, 'ft': 0.3048,
               'g':  1e-3, 'mg': 1e-6, 'μg': 1e-9, 'lb': 0.453592}

def solution(a,b):
    m1, m2, d = starmap(lambda v,u: v * CONVERSIONS.get(u,1), zip(a,b))
    return G * m1 * m2 / (d*d)
"""


"""
convert = {"kg": 1, "g": 1e-3, "mg": 1e-6, "μg": 1e-9, "lb": 0.453592,
           "m": 1, "cm": 1e-2, "mm": 1e-3, "μm": 1e-6, "ft": 0.3048}

def solution(a, b):
    c = [a[i] * convert[b[i]] for i in range(3)]
    return 6.67e-11 * c[0] * c[1] / (c[2] ** 2)
"""
