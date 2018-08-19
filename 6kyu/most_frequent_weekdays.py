import datetime


weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']


def most_frequent_days(year):
    year = str(year) if year > 999 else (4-len(str(year)))*'0' + str(year)
    start_year = year+'-1-1'
    end_year = year+'-12-31'
    starts = datetime.datetime.strptime(start_year, '%Y-%m-%d').weekday()
    ends = datetime.datetime.strptime(end_year, '%Y-%m-%d').weekday()
    return weekdays[starts:ends+1] if starts < ends else weekdays[0:ends+1]+weekdays[starts:7]
    

"""
from calendar import weekday, day_name

def most_frequent_days(year):
    days = [weekday(year, 1, 1), weekday(year, 12, 31)]
    return [day_name[i] for i in sorted(list(set(days)))]
"""


"""
from datetime import datetime
from calendar import day_name


def most_frequent_days(year):
    first = set(range(datetime(year, 1, 1).weekday(), 7))
    last = set(range(datetime(year, 12, 31).isoweekday()))
    return [day_name[day] for day in sorted((first & last) or (first | last))]
"""


"""
from calendar import day_name, isleap, weekday
def most_frequent_days(y):
    first = weekday(y, 1, 1)
    return [day_name[d] for d in sorted([first, (first + 1) % 7][:1 + isleap(y)])]
"""


"""
from calendar import weekday

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']


def most_frequent_days(year):
    beg = weekday(year, 1, 1)
    end = weekday(year, 12, 31)
    return DAYS[beg:end + 1] if beg <= end else DAYS[:end + 1] + DAYS[beg:]
"""

