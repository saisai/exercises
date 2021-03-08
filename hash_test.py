import datetime

"""
a = hash('a')
print(a)

aa = hash('a')
print(aa)


t = [hash('a' + str(i)) for i in range(100000)]

print(t)
"""
#b = frozenset([datetime.date(2019, 3, 1), 4, 1])
#b = "20193141"
#t = hash(b)
#print(t)

t = [(datetime.date(2019, 3, 1), 4, 1), (datetime.date(2019, 3, 2), 5, 1)]

print(t)

