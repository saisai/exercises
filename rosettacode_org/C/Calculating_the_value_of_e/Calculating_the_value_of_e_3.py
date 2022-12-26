
from itertools import (accumulate, chain)
from functools import (reduce)
from operator import (mul)

def eApprox():
    return reduce(
            lambda a, x: a + 1 / x,
            scanl(mul)(1)(
                range(1, 18)
                ),
            0
            )

def main():
    print(
            eApprox()
            )
    
def scanl_org(f):
    return lambda a: lambda xs: (
            accumulate(chain([a], xs), f)
            )

def scanl(f):
    print(type(f), f.__class__.__name__)
    def a(a):
        print(type(a), a.__class__.__name__)
        def xs(xs):
            print(type(xs), xs.__class__.__name__)
            return accumulate(chain([a], xs) , f)
        return xs
    return a

if __name__ == '__main__':
    main()

