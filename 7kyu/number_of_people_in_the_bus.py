def number(bus_stops):
    # Good Luck!
    sum = 0
    for l in bus_stops:
        sum += l[0]-l[1]
    return sum
    
    
"""
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
"""


"""
def number(stops):
    return sum(i - o for i, o in stops)
"""
