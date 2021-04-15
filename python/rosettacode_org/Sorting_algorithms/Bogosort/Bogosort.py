import random


def bogosort(l):
    while not in_order(l):
        random.shuffle(l)
    return l


def in_order(l):
    if not l:
        return True
    last = l[0]
    for x in l[1:]:
        if x < last:
            return False
        last = x
    return True

testset = [100, 10, 2, 99, 5, 6, 11]
print(bogosort(testset))