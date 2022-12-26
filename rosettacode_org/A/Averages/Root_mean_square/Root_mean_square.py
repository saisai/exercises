from math import sqrt
def qmean(num):
	return sqrt(sum(n*n for n in num)/len(num))

print(qmean(range(1,11)))

from functools import (reduce)
from math import (sqrt)


# rootMeanSquare :: [Num] -> Float
def rootMeanSquare(xs):
    return sqrt(reduce(lambda a, x: a + x * x, xs, 0) / len(xs))


print(
    rootMeanSquare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
)