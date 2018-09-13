# Simple Fun #176: Reverse Letter
def reverse_letter(string):
    #do your magic here
    lst = []
    for c in string:
        if c.isalpha():
            lst.append(c)
    return ''.join(lst[::-1])
    
    
“”“
def reverse_letter(s):
  return ''.join([i for i in s if i.isalpha()])[::-1]
”“”


"""
def reverse_letter(string):
    return ''.join(filter(str.isalpha, reversed(string)))
"""
