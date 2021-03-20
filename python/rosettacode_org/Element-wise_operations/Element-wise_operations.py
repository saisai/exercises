import random
from operator import add, sub, mul, floordiv
from pprint import pprint as pp

def ewise(matrix1, matrix2, op):
    return [[op(e1,e2) for e1,e2 in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]


m, n=3, 4

a0 = [[random.randint(1,9) for y in range(n)] for x in range(m)]
a1 = [[random.randint(1,9) for y in range(n)] for x in range(m)]

pp(a0)
pp(a1)

pp(ewise(a0, a1, add))

pp(ewise(a0, a1, sub))
pp(ewise(a0, a1, mul))
pp(ewise(a0, a1, floordiv))
pp(ewise(a0, a1, pow))
pp(ewise(a0, a1, lambda x, y: 2*x-y))


def s_ewise(scalar1, matrix1, op):
    return [[op(scalar1, e1) for e1 in row1] for row1 in matrix1]

scalar = 10
print(a0)

for op in (add, sub, mul, floordiv, pow, lambda x, y:2*x - y):
    print("%10s :" % op.__name__, s_ewise(scalar, a0, op))
