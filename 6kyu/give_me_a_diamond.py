def diamond(n):
    # Make some diamonds!
    rl = []
    if n<3:
        return None
    for i in range(n,0,-2):
        rl.append(' '*((n-i)/2)+'*'*i+'\n')
    rl = rl[::-1]+rl[1:]
    return ''.join(rl)


"""
def diamond(n):
    if not n%2 or n<1: return None
    d = [" "*i+"*"*(n-2*i)+"\n" for i in range(n/2,0,-1)]
    return ''.join(d) + "*"*n + "\n" + ''.join(d[::-1])
"""


"""
def diamond(n):
    if n > 0 and n % 2 == 1:
        return ''.join(' ' * abs((n/2) - i) + '*' * (n - abs((n-1) - 2 * i)) + '\n' for i in range(n))
    return None
"""
