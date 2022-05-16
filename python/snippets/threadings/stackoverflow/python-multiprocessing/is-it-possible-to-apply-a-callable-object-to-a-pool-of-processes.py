
import multiprocessing
'''
class TaskThread:
    def __call__(self):
        print("in TaskThread.__call__")

def main():
    pool = multiprocessing.Pool(4)
    task = TaskThread()
    pool.apply_async(task)
    pool.close()
    pool.join()

def main2():
    pool = multiprocessing.Pool(4)
    task = TaskThread()
    result = pool.apply_async(task)
    result.get()

if __name__ == '__main__':
    main()
    main2()
'''

class TaskThread(object):
    def __init__(self, manager):
        self.queue = manager.Queue()

    def __call__(self):
        print("in TaskThread.__call__")
        self.queue.put(1)

if __name__ == "__main__":
    pool=multiprocessing.Pool(4)
    m = multiprocessing.Manager()
    task=TaskThread(m)
    result = pool.apply_async(task)
    result.get()
    print(task.queue.get())


    # https://stackoverflow.com/questions/26391117/is-it-possible-to-apply-a-callable-object-to-a-pool-of-processes