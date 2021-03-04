from operator import add, mul
from functools import reduce

listoflists = [['the', 'cat'], ['sat', 'on'], ['the', 'mat']]

print(reduce(add, listoflists, []))

nums = range(1, 11)

summation = reduce(add, nums)

product = reduce(mul, nums)

concatenation = reduce(lambda a, b: str(a) + str(b), nums)

print(summation, product, concatenation)
