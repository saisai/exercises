import time
import multiprocessing as mp
import numpy as np

def how_many_within_range(row, minimum, maximum):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count += 1
    return count

if __name__ == '__main__':
    data = np.random.randint(0, 10, size=[1000000, 5])
    print(data[:5])

    # With parallelisation
    start_time = time.perf_counter()
    with mp.Pool() as pool:
        results = pool.starmap(how_many_within_range, ((row,4,8) for row in data), chunksize=1000)
    print(f'Time elapsed: {time.perf_counter() - start_time}')
    print(results[:5])

    # Without parallelisation
    start_time = time.perf_counter()
    results = [ how_many_within_range(row, 4, 8) for row in data ]
    print(f'Time elapsed: {time.perf_counter() - start_time}')
    print(results[:5])
    
    # https://stackoverflow.com/questions/69031731/multiprocessing-code-running-much-slower-than-single-threaded-code