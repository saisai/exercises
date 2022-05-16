from multiprocessing import Process, Queue
import time


def calculate(queue):
    n = 0
    while n < 10:
        n += 1
        queue.put(n)
        time.sleep(1)
    queue.put(0)


def queue_getter(queue):
    executing = True
    while executing:
        while queue.qsize():
            n = queue.get()
            print(n)
            if n == 0:
                executing = False
        time.sleep(0.1)
    print("done")


if __name__ == "__main__":
    queue = Queue()
    p = Process(target=calculate, args=(queue,))
    p.start()
    queue_getter(queue)
    p.join()
    print("DONE")

    # https://stackoverflow.com/questions/71183255/getting-information-back-from-a-process-with-a-multiprocessing-queue