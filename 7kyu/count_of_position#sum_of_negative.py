def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count = 0
    sum = 0 
    for c in arr:
        if c > 0:
            count += 1
        else:
            sum += c
    return [count,sum]
 

"""
def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
"""


"""
def count_positives_sum_negatives(arr):
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []
"""


"""
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []
"""
