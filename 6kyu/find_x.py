"""
# optimize
def find_x(n):
    x = 0
    for i in range(n):
        for j in range(2*n):
            x += i+j
    return x
"""


# optimize
def find_x(n):
    return (3*n-2)*(n**2)
    
    
"""
find_x=lambda n:n*n*(3*n-2)
"""
