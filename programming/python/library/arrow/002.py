from datetime import datetime

import arrow
from dateutil import tz

print('utc now ', arrow.utcnow())
print('now ', arrow.now())
print('Asia/Bangkok ', arrow.now('Asia/Bangkok'))
print(arrow.get(1367900664))
print(arrow.get(1367900664.152325))
print(arrow.get(datetime.utcnow()))
print(arrow.get(datetime(2013, 5, 5), 'US/Pacific'))
print(arrow.get(datetime(2013, 5, 5), 'Asia/Bangkok'))

print(arrow.get(datetime(2013, 5, 5), tz.gettz('Asia/Bangkok')))
print(arrow.get(datetime(2013, 5, 5), tz.gettz('US/Pacific')))
print('now US/Pacific ', arrow.get(datetime.now(tz.gettz('US/Pacific'))))
print('now Asia/Bangkok ', arrow.get(datetime.now(tz.gettz('Asia/Bangkok'))))

print('Parse from a string ', arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss'))
print(type(arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')))
print('Search a date in a string ', arrow.get('June was born in May 1980', 'MMMM YYYY') )

print(arrow.get('2013-09-30T15:34:00.000-07:00'))

print(arrow.get(2013, 5, 5))
print(arrow.Arrow(2013, 5, 5))


