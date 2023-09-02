from itertools import product
from multiprocessing import Pool


def run_test_function(arg1, arg2):
    with Pool(4) as pool:
        pool.starmap(print, product(arg1, arg2), 5)

if __name__ == '__main__':
    run_test_function([1,2,3,4,5], "abc")
    
    # https://stackoverflow.com/questions/68724573/using-parallel-method-instead-of-sequential-loop