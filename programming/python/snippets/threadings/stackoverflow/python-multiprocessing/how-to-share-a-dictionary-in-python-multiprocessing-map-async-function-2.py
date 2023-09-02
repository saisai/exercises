from datetime import datetime
import multiprocessing as mp
import time

time_metrics = {}

def g(a):
    for i in range(5000*a):
        pass


def f(idx):
    a = datetime.utcnow()
    g(idx)
    time.sleep(1)
    b = datetime.utcnow()
    return (idx, b - a)


def append_res(result: tuple):
    for row in result:
        time_metrics[row[0]] = row[1]


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6]
    # don't assign 1 process for each job, use only number of cores your machine has, as rarely any benefit of using more, especially for benchmarking.
    with mp.Pool(3) as pool:
        # doesn't block until result is available.
        # callback is applied to list of results when all the tasks are complete
        results = pool.map_async(f, lst, callback = append_res)
        # wait for result to become available, otherwise parent process will exit the context manager and processes will not complete
        results.wait()
    
    print(time_metrics)