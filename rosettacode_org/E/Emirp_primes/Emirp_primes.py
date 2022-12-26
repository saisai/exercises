from __future__ import print_function
from Prime_decomposition import primes, is_prime
from heapq import *
from itertools import islice
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)



def emirp():
    largest = set()
    emirps = []
    heapify(emirps)
    for pr in primes():
        while emirps and pr > emirps[0]:
            #print('test ', emirps, emirps[0], pr)
            logging.debug('test %s %s %s' % (emirps, emirps[0], pr))
            yield heappop(emirps)
        if pr in largest:
            yield pr
        else:
            rp = int(str(pr)[::-1])
            if rp > pr and is_prime(rp):
                heappush(emirps, pr)
                largest.add(rp)


print('First 20:\n  ', list(islice(emirp(), 20)))
print('Between 7700 and 8000:\n  [', end='')
for pr in emirp():
    if pr >= 8000: break
    if pr >= 7700: print(pr, end=', ')
print(']')
print('10000th:\n  ', list(islice(emirp(), 10000 - 1, 10000)))