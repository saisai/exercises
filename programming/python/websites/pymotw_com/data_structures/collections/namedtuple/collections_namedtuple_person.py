import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)

print('\nRepresentation:', bob)

jane = Person(name='Jane', age=29)
print('\nField by name:', jane.name)

print('aa')
print(str(jane), type(str(jane)))

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is {} years old'.format(*p))

