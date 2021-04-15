import operator
import random
from itertools import dropwhile, islice, repeat, starmap


def shuffled(x):
    x = x[:]
    random.shuffle(x)
    return x


bogosort = lambda l: next(dropwhile(
    lambda l: not all(starmap(operator.le, zip(l, islice(l, 1, None)))),
    map(shuffled, repeat(l))))


testset = [100, 10, 2, 99, 5, 6, 11]
print(bogosort(testset))