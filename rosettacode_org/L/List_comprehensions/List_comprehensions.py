
n = 10
t = [(x,y,z) for x in range(1,n+1) for y in range(x,n+1) for z in range(y,n+1) if x**2 + y**2 == z**2]

print(t)


b = ((x,y,z) for x in range(1,n+1) for y in range(x,n+1) for z in range(y,n+1) if x**2 + y**2 == z**2)
print(b)
print(list(b))

import itertools
c = [(x, y, z) for (x, y, z) in itertools.product(range(1,n+1),repeat=3) if x**2 + y**2 == z**2 and x <= y <= z]

print(c)

d = ((x, y, z) for (x, y, z) in itertools.product(range(1,n+1),repeat=3) if x**2 + y**2 == z**2 and x <= y <= z)

print(d)
print(list(d))


def triplets(n):
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            for z in range(y, n + 1):
                yield x, y, z

e = [(x, y, z) for (x, y, z) in triplets(n) if x**2 + y**2 == z**2]
print(e)

f = ((x, y, z) for (x, y, z) in triplets(n) if x**2 + y**2 == z**2)
print(f)