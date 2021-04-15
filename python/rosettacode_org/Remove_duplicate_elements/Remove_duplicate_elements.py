items = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']
unique = list(set(items))
print(unique)


items = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']
unique2 = []
helperset = set()
for x in items:
    if x not in helperset:
        unique2.append(x)
        helperset.add(x)

print(unique2)



import itertools
items = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']
#items = list(map(str, items))
#print(items)

def hello(val):
    print("test " + str(val))

unique3 = [k for k,g in itertools.groupby(sorted(items, key=str))]
print(unique3)

# If both of the above fails, we have to use the brute-force method, which is inefficient:
items = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']
unique4 = []
for x in items:
    if x not in unique4:
        unique4.append(x)

print(unique4)

from collections import OrderedDict as od

print(list(od.fromkeys([1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']).keys()))

