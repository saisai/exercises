# nubBy :: (a -> a -> Bool) -> [a] -> [a]
def nubBy(p, xs):
    def go(xs):
        if xs:
            x = xs[0]
            return [x] + go(
                list(filter(
                    lambda y: not p(x, y),
                    xs[1:]
                ))
            )
        else:
            return []
    return go(xs)

xs = [
    'apple', 'apple',
    'ampersand', 'aPPLE', 'Apple',
    'orange', 'ORANGE', 'Orange', 'orange', 'apple'
]
for eq in [
    lambda a, b: a == b,  # default case sensitive uniqueness
    lambda a, b: a.lower() == b.lower(),  # case-insensitive uniqueness
    lambda a, b: a[0] == b[0],  # unique first char (case-sensitive)
    lambda a, b: a[0].lower() == b[0].lower(),  # unique first char (any case)
]:
    print(
        nubBy(eq, xs)
    )