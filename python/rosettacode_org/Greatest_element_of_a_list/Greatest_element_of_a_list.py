floatstrings = ['1\n', ' 2.3\n', '4.5e-1\n', '0.01e4\n', '-1.2']
print(max(floatstrings, key=float))

print(max(float(x) for x in floatstrings))

mylist = [47, 11, 42, 102, 13]

from functools import reduce
result = reduce(lambda a, b: a if (a > b) else b, mylist)
print(result)
