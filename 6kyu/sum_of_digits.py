def digital_root(n):
    while n >= 10:
        n=sum(map(int,str(n)))
        digital_root(n)
    return n
    

"""
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
"""


"""
def digital_root(n):
    return n%9 or n and 9 
“”“


”“”
def digital_root(n):
    return 1 + ((int(n) - 1) % 9) if n>0 else 0
“”“


“”“
def digital_root(n):
    while n >= 10:
        n = sum(divmod(n, 10))
    return n
”“”
