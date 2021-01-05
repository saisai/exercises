numbers = [1, 2, 3]

total = sum(numbers)
print(total)

product = 1
for i in numbers:
    product *= i

print(product)

from operator import mul, add
from functools import reduce

summer = reduce(add, numbers) # note: this version doesn't work with empty lists
print(summer)

summer2 = reduce(add, numbers, 0)
print(summer2)

product = reduce(mul, numbers) # note: this version doesn't work with empty lists
print(product)
product = reduce(mul, numbers, 1)
print(product)


from numpy import r_

numbers = r_[1:4]
total = numbers.sum()
print(total)

product = numbers.prod()
print(product)


import math
total = math.fsum(numbers)
print(total)
