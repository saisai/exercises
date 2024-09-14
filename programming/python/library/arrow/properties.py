from datetime import datetime

import arrow

a = arrow.utcnow()
print(a.datetime)
print(type(a.datetime))
print(a.date())
print(a.naive)
print(a.tzinfo)
print(a.year)
print(a.time())

print(arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ'))

start = datetime(2013, 5, 5, 12, 30)
end = datetime(2013, 5, 5, 17, 15)
for r in arrow.Arrow.span_range('hour', start, end):
    print(r)
    print(repr(r))


start = datetime(2013, 5, 5, 12, 30)
end = datetime(2013, 5, 5, 17, 15)
for r in arrow.Arrow.range('hour', start, end):
    print(r)
    print(repr(r))
