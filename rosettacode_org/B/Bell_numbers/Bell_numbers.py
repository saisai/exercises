
from itertools import accumulate, chain, islice
from operator import add, itemgetter
from functools import reduce

def bellNumbers():
    return map(itemgetter(0), bellTriangle())

def bellTriangle():
    return map(
        itemgetter(1),
        iterate(
            compose(
                bimap(last)(identity),
                list, uncurry(scanl(add))
                )
            )((1, [1]))
        )

def main():
    showIndex = compose(repr, succ, itemgetter(0))
    showValue = compose(repr, itemgetter(1))
    print(
        fTable(
            'First fifteen Bell numbers:'
        )(showIndex)(showValue)(identity)(list(
            enumerate(take(15)(bellNumbers()))
        ))
    )
    print('\nFiftieth Bell number:')
    bells = bellNumbers()
    drop(49)(bells)
    print(
        next(bells)
    )
    print(
        fTable(
            "\nFirst 10 rows of Bell's triangle:"
        )(showIndex)(showValue)(identity)(list(
            enumerate(take(10)(bellTriangle()))
        ))
    )

def bimap(f):
    def go(g):
        def gox(x):
            return (f(x), g(x))
        return gox
    return go

def compose(*fs):
    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, identity)

def drop(n):
    def go(xs):
        if isinstance(xs, (list, tuple, str)):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return go

def fTable(s):
    def gox(xShow):
        def gofx(fxShow):
            def gof(f):
                def goxs(xs):
                    ys = [xShow(x) for x in xs]
                    w = max(map(len, ys))

                    def arrowed(x, y):
                        return y.rjust(w, ' ') + ' -> ' + fxShow(f(x))
                    return s + '\n' + '\n'.join(
                        map(arrowed, xs, ys)
                    )
                return goxs
            return gof
        return gofx
    return gox

def identity(x):
    return x

def iterate(f):
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go

def last(xs):
    return xs[-1]

def scanl(f):
    def go(a):
        def g(xs):
            return accumulate(chain([a], xs), f)
        return g
    return go

def succ(x):
    return 1 + x

def take(n):
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


def uncurry(f):
    def go(tpl):
        return f(tpl[0])(tpl[1])
    return go

if __name__ == '__main__':
    main()

