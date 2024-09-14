import threading
import time

def worker(barrier):
    print(threading.current_thread().name,
          'waiting for barrier with {} others'.format(
              barrier.n_waiting
          ))
    worker_id = barrier.wait()
    print(threading.current_thread().name, 'after barrier',
          worker_id)


NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS)

threads = [
    threading.Thread(
        target=worker,
        name='worker-%s' % i,
        args=(barrier,)
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, 'staring')
    t.start()
    time.sleep(0.1)

for t in threads:
    t.join()
