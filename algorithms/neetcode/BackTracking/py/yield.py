
import pdb
def hello():

    pdb.set_trace()

    t = 0

    for i in [1, 2, 3]:
        yield i
        t += i
    return 't ', t

print(list(hello()))

