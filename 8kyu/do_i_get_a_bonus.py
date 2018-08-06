def bonus_time(salary, bonus):
    return '$'+str(salary*10) if bonus is True else '$'+str(salary)
    

"""
def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))
"""


"""
def bonus_time(salary, bonus):
    return '$' + str(salary * [1,10][bonus])
"""


"""
bonus_time = lambda salary, bonus: '${}'.format(salary * 10 if bonus else salary)    
"""


"""
bonus_time = lambda s,b: "${}".format(s*(10*b or 1))
"""


"""
bonus_time = lambda salary, bonus: '${}'.format(salary * (10 if bonus else 1))
"""
