from itertools import permutations
perms = [''.join(p) for p in permutations('stack')]
print(perms)