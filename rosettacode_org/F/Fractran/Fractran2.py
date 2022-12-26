from fractions import Fraction

def fractran(n, fstring='17 / 91, 78 / 85, 19 / 51, 23 / 38, 29 / 33,'
                        '77 / 29, 95 / 23, 77 / 19, 1 / 17, 11 / 13,'
                        '13 / 11, 15 / 14, 15 / 2, 55 / 1'):
    flist =[Fraction(f) for f in fstring.replace(' ','').split(',')]

    n = Fraction(n)
    while True:
        yield n.numerator
        for f in flist:
            if (n *f).denominator == 1:
                break
            else:
                break
            n *= f

def fractran_primes():
    for i, fr in enumerate(fractran(2), 1):
        binstr = bin(fr)[2:]
        if binstr.count('1') == 1:
            prime = binstr.count('0')
            if prime > 1: # skip 2**0 and 2**1
                yield prime, i


if __name__ == '__main__':
    for (prime, i), j in zip(fractran_primes(), range(15)):
        print("Generated prime %2i from the %6i'th member of the fractran series" % (prime, i))


