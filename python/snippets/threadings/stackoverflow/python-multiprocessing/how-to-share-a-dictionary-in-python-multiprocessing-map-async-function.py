from datetime import datetime
import multiprocessing as mp

time_metrics = {}

def g(a):
    # placeholder function for whatever you have as g()
    for i in range(5000*a):
        pass


def f(idx):
    # once spawned, a process calling this function cannot edit objects in the memory of the parent process, 
    # unless using the special shared memory objects in the mp class.
    a = datetime.utcnow()
    g(idx)
    b = datetime.utcnow()
    return (idx, b - a)


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6]
    # don't assign 1 process for each job, use only number of cores your machine has, as rarely any benefit of using more, especially for benchmarking.
    with mp.Pool() as pool:
        # blocks until result is available
        results = pool.map(f, lst)

    for row in results:
        time_metrics[row[0]] = row[1]
    
    print(time_metrics)