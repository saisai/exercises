'''
For this example, loop over the arrays:

    (a,b,c)
    (A,B,C)
    (1,2,3)
to produce the output:

    aA1
    bB2
    cC3
'''
print ( '\n'.join(''.join(x) for x in
zip('abc', 'ABC', '123')) )

print('\n')
print(*map(''.join, zip('abc', 'ABC', '123')), sep='\n')

from itertools import zip_longest
print ( '\n'.join(''.join(x) for x in zip_longest('abc',
'ABCD', '12345', fillvalue='#')) )