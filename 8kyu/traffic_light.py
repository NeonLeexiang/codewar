def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


"""
update_light = {"green":"yellow", "yellow":"red", "red":"green"}.get
"""


"""
def update_light(current):
    color = ['green', 'yellow', 'red']
    return color[(color.index(current)+1)%len(color)]
"""
