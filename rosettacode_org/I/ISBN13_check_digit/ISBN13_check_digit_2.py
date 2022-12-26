'''ISBN13 check digit'''

from itertools import cycle
from operator import mul


# isISBN13 :: String -> Bool
def isISBN13(s):
    '''True if the digits of s form
       a valid ISBN-13 code.
    '''
    digits = [int(c) for c in s if c.isdigit()]
    return 13 == len(digits) and 0 == sum(
        map(
            mul,
            digits,
            cycle([1, 3])
        )
    ) % 10


# ---------------------------TEST---------------------------
# main :: IO ()
def main():
    '''Validation of four strings:'''

    for s in ['978-1734314502', '978-1734314509',
              '978-1788399081', '978-1788399083']:
        print((s, isISBN13(s)))


# MAIN ---
if __name__ == '__main__':
    main()

