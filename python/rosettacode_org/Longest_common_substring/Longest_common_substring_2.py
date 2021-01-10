from itertools import (accumulate, chain)
from functools import reduce

def longestCommon(s1):
    return lambda s2: max(intersect(
        *map(lambda s: map(
            concat,
            concatMap(tails)(
                compose(tail)(inits)(s)
            )
        ), [s1, s2])
    ), key=len)

# TEST ----------------------------------------------------
def main():
    print(
        longestCommon("testing123testing")(
            "thisisatest"
        )
    )


# GENERIC -------------------------------------------------


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    return lambda f: lambda x: g(f(x))


# concat :: [String] -> String
def concat(xs):
    return ''.join(chain.from_iterable(xs))


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    return lambda xs: list(
        chain.from_iterable(
            map(f, xs)
        )
    )


# inits :: [a] -> [[a]]
def inits(xs):
    return scanl(lambda a, x: a + [x])(
        []
    )(list(xs))


# intersect :: [a] -> [a] -> [a]
def intersect(xs, ys):
    s = set(ys)
    return [x for x in xs if x in s]


# map :: (a -> b) -> [a] -> [b]
def map_(f):
    return lambda xs: list(map(f, xs))


# scanl is like reduce, but returns a succession of
# intermediate values, building from the left.
# scanl :: (b -> a -> b) -> b -> [a] -> [b]


def scanl(f):
    return lambda a: lambda xs: (
        list(accumulate([a] + list(xs), f))
    )


# tail :: [a] -> [a]
def tail(xs):
    return xs[1:]


# tails :: [a] -> [[a]]
def tails(xs):
    return list(map(
        lambda i: xs[i:],
        range(0, 1 + len(xs))
    ))


# MAIN ---
main()
