import multiprocessing
import numpy as np
import time

def getData(queue):

    KEY_PRESSED = False

    expiration = time.time() + 5
    # Run for 5 seconds:
    while KEY_PRESSED is False:

        if time.time() > expiration:
            queue.put(None)
            print("STOP in getData")
            KEY_PRESSED=True
        else:
            data = np.random.random([8, 250])
            queue.put(data)

def processData(queue):

    FLAG_STOP = False

    t = time.time()
    cnt = 0
    while FLAG_STOP is False:
        data = queue.get()  # # ch, samples
        if data is None:
            print("STOP in processData")
            print('Number of items read from queue:', cnt, 'elapsed_time:', time.time() - t)
            FLAG_STOP = True
        else:
            cnt += 1
            print("Processing Data")
            print(str(data[0,0]))

if __name__ == "__main__":

    queue = multiprocessing.Queue()
    processes = [
        multiprocessing.Process(target=getData, args=(queue,)),
        multiprocessing.Process(target=processData, args=(queue,))
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
        
    https://stackoverflow.com/questions/69992497/how-to-detect-a-pressed-key-within-python-process