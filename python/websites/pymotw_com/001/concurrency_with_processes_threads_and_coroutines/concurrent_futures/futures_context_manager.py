from concurrent import futures
import threading
import time
from datetime import datetime

def task(n):
    for _ in range(10):
        print('{}-{}'.format(threading.current_thread().name , n))
    now = datetime.now()
    print(now)


with futures.ThreadPoolExecutor(max_workers=100) as ex:
    print('main: starting')
    for i in range(100):
        ex.submit(task, i)

    """    
    ex.submit(task, 1)
    ex.submit(task, 2)
    ex.submit(task, 3)
    ex.submit(task, 4)
    """

print('main: done')