import numpy as np
from time import sleep
import os

def f(r):
    res = np.arange(r[0], r[1])
    print(f'I am {os.getpid()}')
    sleep(10)
    print(f'I am {os.getpid()} and I am finished')
    return {'nums': res, 'dubs': res * 2}

import multiprocessing as mp
import numpy as np
#from fs import f

'''
if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    p = ctx.Pool(4)
    with p:
        subsets = [[0, 3], [3, 6], [6, 7]]
        res = [p.apply(f, (subset, )) for subset in subsets]
        print(res)

    print('Done!')
'''
'''
#working
if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    with ctx.Pool(4) as p:
        subsets = [[0, 3], [3, 6], [6, 7]]
        res = p.map(f, subsets)
        print(res)
        
    print('Done!')
'''

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    with ctx.Pool(4) as p:
        subsets = [[0, 3], [3, 6], [6, 7]]

        items = [p.apply_async(f, (subset, )) for subset in subsets]
        print(items)
        
        res = [x.get() for x in items]
        print(res)
        
    print('Done!')
    
    # https://stackoverflow.com/questions/69620568/parallelization-using-multiprocessing-running-processes-sequentially-instead-of