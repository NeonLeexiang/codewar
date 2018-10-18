def isLeapYear(year):
    #your code here. Try to do it in one line.
    if year%100 == 0 and year%400 !=0:
        return False
    elif year%400 == 0:
        return True
    return year%4 == 0


"""
def isLeapYear(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
"""


"""
from calendar import isleap as isLeapYear
"""
