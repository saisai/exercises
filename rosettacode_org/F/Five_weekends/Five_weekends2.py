from datetime import timedelta, date
 
DAY     = timedelta(days=1)
START, STOP = date(1900, 1, 1), date(2101, 1, 1)
WEEKEND = {6, 5, 4}     # Sunday is day 6
FMT     = '%Y %m(%B)'
 
def fiveweekendspermonth(start=START, stop=STOP):
    'Compute months with five weekends between dates'
 
    when = start
    lastmonth = weekenddays = 0
    fiveweekends = []
    while when < stop:
        year, mon, _mday, _h, _m, _s, wday, _yday, _isdst = when.timetuple()
        if mon != lastmonth:
            if weekenddays >= 15:
                fiveweekends.append(when - DAY)
            weekenddays = 0
            lastmonth = mon
        if wday in WEEKEND:
            weekenddays += 1
        when += DAY
    return fiveweekends
 
dates = fiveweekendspermonth()


LONGMONTHS = (1, 3, 5, 7, 8, 10, 12) # Jan Mar May Jul Aug Oct Dec
def fiveweekendspermonth2(start=START, stop=STOP):
    return [date(yr, month, 31)
            for yr in range(START.year, STOP.year)
            for month in LONGMONTHS
            if date(yr, month, 31).timetuple()[6] == 6 # Sunday
            ]


dates2 = fiveweekendspermonth2()
assert dates2 == dates

