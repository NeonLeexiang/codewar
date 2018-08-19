def reverse_number(n):
    return int(str(n)[::-1]) if n > 0 else 0 - int(str(abs(n))[::-1])


"""
def reverseNumber(n):
    if n < 0: return -reverseNumber(-n)
    return int(str(n)[::-1])
"""


"""
def reverseNumber(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)
"""


"""
reverseNumber = lambda n: int(str(n)[::-1]) if n >= 0 else -reverseNumber(-n)
"""
