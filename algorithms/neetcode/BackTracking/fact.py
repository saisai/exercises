import pdb
def fact(n):
    pdb.set_trace()
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(3))