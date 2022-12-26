values = range(10)
print(values)
evens = [x for x in values if not x & 1]
print(evens)
ievens = (x for x in values if not x & 1) # lazy
print(ievens)
# alternately but less idiomatic:
evenss = filter(lambda x: not x & 1, values)
print(evenss)
print(list(evenss))
print(values[::2])
for i in values[::3]:
    print(i)

valuess = list(range(10))
print(valuess[::2])
print(valuess[0::2])
print(valuess[1::2])
valuess[::2] = [11,13,15,17,19]
print(valuess)
print(valuess[0::2])
print(valuess[1::2])

