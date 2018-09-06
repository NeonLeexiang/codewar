def solution(number):
    rt = 0
    for i in range(number):
        if i%3 == 0 or i%5 == 0:
            rt += i
    return rt
    

"""
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""


"""
def solution(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result
"""
