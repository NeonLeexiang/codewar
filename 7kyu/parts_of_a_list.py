def partlist(arr):
    return [(' '.join(arr[:i]),' '.join(arr[i:])) for i in range(1,len(arr))]


"""
Mine is the same as the solution of codewar
"""
