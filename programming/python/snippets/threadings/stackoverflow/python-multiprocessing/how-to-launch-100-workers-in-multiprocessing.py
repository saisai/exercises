'''
How to launch 100 workers in multiprocessing?
'''

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(20) as p:
        print(p.map(f, range(100)))
    
    # https://stackoverflow.com/questions/70626493/how-to-launch-100-workers-in-multiprocessing