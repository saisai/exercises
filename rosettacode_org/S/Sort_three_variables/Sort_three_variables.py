while True:
    x, y, z = eval(input('Three Python values: '))
    print(f'As read: x = {x!r}; y = {y!r}; z = {z!r}')
    x, y, z = sorted((x, y, z))
    print(f' Sorted: x = {x!r}; y = {y!r}; z = {z!r}')

"""
Three Python values: 3, 2, 1
As read: x = 3; y = 2; z = 1
 Sorted: x = 1; y = 2; z = 3

Three Python values: 'lions, tigers, and', 'bears, oh my!', '(from the "Wizard of OZ")'
As read: x = 'lions, tigers, and'; y = 'bears, oh my!'; z = '(from the "Wizard of OZ")'
 Sorted: x = '(from the "Wizard of OZ")'; y = 'bears, oh my!'; z = 'lions, tigers, and'

Three Python values: 77444, -12, 0
As read: x = 77444; y = -12; z = 0
 Sorted: x = -12; y = 0; z = 77444
"""