def in_asc_order(arr):
    # random_ is not allowed
    return arr == sorted(arr)


"""
def in_asc_order(a):
    return all(x < y for x, y in zip(a, a[1:]))
"""


"""
in_asc_order = lambda l: sorted(l) == l
"""
