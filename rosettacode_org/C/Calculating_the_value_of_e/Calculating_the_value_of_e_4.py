

from functools import reduce

def eApprox(n):
    def go(efl, x):
        e, fl = efl
        flx = fl * x
        return e + 1 / flx, flx

    return reduce(
            go,
            range(1, 1 + n),
            (1, 1)
            )[0]

def main():
    print(eApprox(20))

if __name__ == '__main__':
    main()

