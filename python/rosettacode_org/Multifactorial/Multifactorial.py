from functools import reduce
from operator import mul
def mfac(n, m): return reduce(mul, range(n, 0, -m))

for m in range(1, 11):
    print("%2i: %r" % (m, [mfac(n, m) for n in range(1, 11)]))

