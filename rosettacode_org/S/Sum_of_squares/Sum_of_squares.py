
test = [1, 2, 3, 4, 5]
# using generator expression
print(sum(x * x for x in test))

# or
print(sum(x ** 2 for x in test))

# or


print(sum(pow(x, 2) for x in test))

# using functional versions
# using lambda and map
print(sum(map(lambda x: x * x, test)))

# or
print(sum(map(lambda x: x ** 2 , test)))

# or 
print(sum(map(lambda x: pow(x, 2), test)))

# using pow and repeat
from itertools import repeat
print(sum(map(pow, test, repeat(2))))

# using starmap and mul
from itertools import starmap
from operator import mul
print(sum(starmap(mul, zip(test, test))))


# using reduce
from functools import reduce
powers_of_two = (x * x for x in test)

print(reduce(lambda x, y: x + y, powers_of_two))

# or
from operator import add
powers_of_two = (x * x for x in test)
print(reduce(add, powers_of_two))

# or using a bit more complex lambda
print(reduce(lambda a, x: a + x*x, test))
