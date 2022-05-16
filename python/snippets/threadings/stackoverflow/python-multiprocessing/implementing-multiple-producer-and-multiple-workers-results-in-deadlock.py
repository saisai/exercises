from multiprocessing import Process, JoinableQueue
from time import sleep


def consumer(in_queue: JoinableQueue, out_queue: JoinableQueue):
    while True:
        item = in_queue.get()
        sleep(0.5)
        s = str(item)
        out_queue.put(s)
        in_queue.task_done()

def producer(in_queue: JoinableQueue):
    while True:
        item = in_queue.get()
        sleep(0.5)
        n = int(item)
        print(n)
        in_queue.task_done()

if __name__ == "__main__":
    number_queue = JoinableQueue()
    str_queue = JoinableQueue()

    for _ in range(4):
        Process(target=consumer, args=(number_queue, str_queue), daemon=True).start()
        Process(target=producer, args=(str_queue,), daemon=True).start()

    for i in range(100):
        number_queue.put(i)

    number_queue.join()
    str_queue.join()