"""
http://rosettacode.org/wiki/Loop_over_multiple_arrays_simultaneously#Python
"""

print('\n'.join(''.join(x) for x in zip('abc', 'ABC', '123')))


print(*map(''.join, zip('abc', 'ABC', '123')), sep='\n')


print()


def join3(a, b, c):
    return a + b + c

print(list(map(join3, 'abc', 'ABC', '123')))


from itertools import zip_longest

print('\n'.join(''.join(x) for x in zip_longest('abc', 'ABCD', '12345', fillvalue='#')))
