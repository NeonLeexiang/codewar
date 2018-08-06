"""
import re

def is_matched(read):
    total = sum([int(num) for num in re.findall(r'\d+', read[0])])
    
    if read[0] == str(len(read[1])) + 'M':
        return True
    elif len(read[1]) != total:
        return 'Invalid cigar'
    else:
        return False
"""
 
 
"""
import re

def is_matched(read):
    cigar, seq = read
    matches = re.findall(r'(\d+)([A-Z])', cigar)
    if sum(int(n) for n, _ in matches) != len(seq):
        return 'Invalid cigar'
    return all(sym == 'M' for _, sym in matches)
"""
 
 
"""
is_matched=lambda s:(lambda a,b:'Invalid cigar'if sum(map(int,__import__('re').findall('\d+',a)))!=len(b)else a==str(len(b))+'M')(*s)
"""
 
 
"""
import re
def is_matched(read):
    num = re.compile(r'\d+')
    a = list(map(int,num.findall(read[0])))
    Dna_length = sum(a[0:len(a)])
    if Dna_length != len(read[1]):      
        return "Invalid cigar"
    else:
        return a[0] == len(read[1]) and str(a[0])+"M" == read[0]
"""


"""
import re
def is_matched(read):
    match, base = read
    s=match
    index = match.find('M')
    match = match[:index]
    
    l = (re.findall('\d+', s))
    total = sum([int(x) for x in l])

    if total != len(base):
        return('Invalid cigar')
    if 'M'  in s and len(base) == int(match):
        return(True)
    elif 'M' not in s or int(match) < len(base) and len(base) != int(match):
        return(False)
"""


"""
def is_matched(s):
    a,b=s
    A=''.join((' ',x)[x.isdigit()]for x in a).split()
    return'Invalid cigar'if sum(map(int,A))!=len(b)else(int(a.split('M')[0])if'M'in a else 0)==len(b)
"""
