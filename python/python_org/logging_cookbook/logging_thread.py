import logging
import threading
import time

def worker(arg, barrier):

    worker_id = barrier.wait()
    while not arg['stop']:
        logging.debug("Hi from myfunc %s", worker_id)
        time.sleep(0.5)


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(relativeCreated)6d %(threadName)s %(message)s'
                        )
    info = {'stop': False}
    NUM_THREADS = 5

    #thread = threading.Thread(target=worker, args=(info,))
    #thread.start()

    barrier = threading.Barrier(NUM_THREADS)

    threads = [
        threading.Thread(
            name="worker-%s" % i,
        target=worker, args=(info,barrier,),
        )for i in range(NUM_THREADS)]

    for t in threads:
        t.start()
        time.sleep(0.1)


    while True:
        try:
            logging.debug("Hello from main")
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    #thread.join()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
