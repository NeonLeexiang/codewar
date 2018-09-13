# Simple Fun #40: Timed Reading


import re
import string


def timed_reading(max_length, text):
  #coding and coding..
  t = re.sub("[{}]+".format(string.punctuation), "", text).split(" ")
  
  count = 0
  
  for c in t:
      if len(c) <= max_length and len(c) > 0:
          count += 1 
  return count
  
  
"""
import re
def timed_reading(max_length, text):
    return sum(len(i) <= max_length for i in re.findall('\w+', text))
"""


"""
import re

def timed_reading(max_length, text):
    return sum( len(m.group()) <= max_length for m in re.finditer(r'\w+', text))
"""
