
from functools import reduce


def tokenize(delim):


    def go(esc, s):

        def chop(a, x):
            tkn, xs, escaped = a
            literal = not escaped
            isEsc = literal and (esc == x)
            return ([], [tkn] + xs, isEsc) if (
                literal and (delim == x)
            ) else (tkn if isEsc else [x] + tkn, xs, isEsc)

        tkn, xs, _ = reduce(chop, list(s), ([], [], False))

        return list(reversed(
            [''.join(reversed(x)) for x in [tkn] + xs]
        ))
    return lambda esc: lambda s: go(esc, s)




    return go(esc, s)

    #return go(esc, s)


def main():

    print(
        tokenize('|')('^')(
            "one^|uno||three^^^^|four^^^|^cuatro|"
        )
    )

if __name__ == '__main__':
    main()
