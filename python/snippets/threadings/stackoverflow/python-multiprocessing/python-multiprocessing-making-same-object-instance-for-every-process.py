import time
import multiprocessing as mp
import os


class SomeOtherClass:

    def __new__(cls, *args, **kwargs):
        print('-- inside __new__ --')
        return super(SomeOtherClass, cls).__new__(cls, *args, **kwargs)


    def __init__(self):
        self.a = os.getpid()
    def __str__(self):
        return f'{self.a}'


class SomeProcessor(mp.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        soc = SomeOtherClass()
        print("PID: ", os.getpid())
        print(soc)

if __name__ == "__main__":
    queue = mp.Queue()

    for n in range(10):
        queue.put(n)

    processes = []

    for proc in range(mp.cpu_count()):
        p = SomeProcessor(queue)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        
    # https://stackoverflow.com/questions/69087228/python-multiprocessing-making-same-object-instance-for-every-process