from math import sqrt

def factor(n):
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

for i in (45, 53, 64): print( "%i: factors: %s" % (i, factor(i)) )