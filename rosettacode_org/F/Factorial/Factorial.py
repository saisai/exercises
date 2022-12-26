import math

def fact(n):

    print(math.factorial(n))


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def functional(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1), 1)

def functional_1(n):
    from itertools import (accumulate, chain)
    from operator import mul

    return list(
        accumulate(chain([1], range(1, 1+n)), mul)
    )[-1]

def functional_2(n):
    from itertools import (accumulate, chain)
    from operator import mul

    return list(
        accumulate(chain([1], range(1, 1+n)), mul)
    )

def fact_2(n):
    from numpy import prod

    return prod(range(1, n + 1), dtype=int)


def fact_3(n):
    z = 1
    if n > 1:
        z = n * fact_3(n-1)
    return z

def fact_4(n):
    return n * fact_4(n-1) if n else 1

if __name__ == '__main__':
    fact(10)
    print(factorial(10))
    print(functional(10))
    print(functional_1(10))
    print(functional_2(10))
    print(fact_2(10))
    print(fact_3(10));
    print(fact_4(10))
