from operator import *

class MyObj:
    """Example class for attrgetter"""

    def __init__(self, arg):
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

l = [MyObj(i) for i in range(5)]
print('objects :', l)

# Extract the 'arg' value from each object
g = attrgetter('arg')
print('g' , g)
vals = [g(i) for i in l]
print('arg values:', vals)

# Sort using arg
l.reverse()
print('reversed :', l)
print('sorted :', sorted(l, key=g))

