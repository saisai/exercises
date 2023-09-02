from multiprocessing import Pool
from time import sleep

def sleeping(i):
    print(f"{i} started")
    sleep(5)
    print(f"{i} ended")

if __name__ == "__main__":
    with Pool(processes=5) as p:
        results = [p.apply_async(sleeping, args=(i,)) for i in range(10)]
        results = [result.get() for result in results]