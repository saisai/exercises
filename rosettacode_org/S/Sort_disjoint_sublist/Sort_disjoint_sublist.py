def disjointSort(ixs):

    def go(xs):
        ks = sorted(ixs)
        dct = dict(zip(ks, sorted(xs[k] for k in ks)))
        return [
            dct[i] if i in dct else x
            for i, x in enumerate(xs)
        ]
    return go


def main():
    '''Disjoint sublist at three indices.'''
    print(
        tabulated(
            "Disjoint sublist at indices [6, 1, 7] sorted:\n"
        )(str)(str)(
            disjointSort([6, 1, 7])
        )([
            [7, 6, 5, 4, 3, 2, 1, 0],
            ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
        ])
    )


def tabulated(s):
    def go(xShow, fxShow, f, xs):
        w = map(map(compose(len)(xShow), xs))

        return s + '\n' + '\n'.join(
                    xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x) for x in xs)
                )
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )


def compose(g):
    """Function compposition"""
    return lambda f: lambda x: g(f(x))

if __name__ == '__main__':
    main()
