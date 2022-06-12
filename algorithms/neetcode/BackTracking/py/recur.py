
import pdb

def recur(n):
    pdb.set_trace()
    if n <= 1:
        return n
    else:
        return (recur(n - 1) + recur(n - 2))


print(recur(3))
