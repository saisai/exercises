# isHappy :: Int -> Bool
def isHappy(n):
    '''Happy number sequence starting at n reaches 1 ?'''
    seen = set()

    # p :: Int -> Bool
    def p(x):
        if 1 == x or x in seen:
            return True
        else:
            seen.add(x)
            return False

    # f :: Int -> Int
    def f(x):
        print('x ', x)
        print(sum(int(d) ** 2 for d in str(x)))
        return sum(int(d) ** 2 for d in str(x))
    print(until(p)(f)(n))
    return 1 == until(p)(f)(n)

# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.'''
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)

print(isHappy(11))