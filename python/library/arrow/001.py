import arrow

print(arrow.get('2013-05-11T21:23:58.970460+07:00'))


utc = arrow.utcnow()
print(utc)

utc = utc.shift(hours=-1)
print(utc)

local = utc.to('US/Pacific')
print(local)

local = utc.to('Asia/Bangkok')
print('bangkok ', local)

utc2 = arrow.utcnow()
print(utc2)
local = utc2.to('Asia/Bangkok')
print('bangkok ', local)


print(local.timestamp())
print(local.format())

print(local.format('YYYY-MM-DD HH:mm:ss ZZ'))

print(local.humanize())

print(local.humanize(locale='ko-kr'))


print(arrow.utcnow())
