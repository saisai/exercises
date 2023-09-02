import multiprocessing
import keyboard
import time

def getData(queue_raw):
    for num in range(1000):
        queue_raw.put(num)
        print("getData: put "+ str(num)+" in queue_raw")
    while True:
        if keyboard.read_key() == "s":
            break

def calcFeatures(queue_raw, queue_features):
    '''
    while not queue_raw.empty():
        data = queue_raw.get()
        queue_features.put(data**2)
        print("calcFeatures: put "+ str(data**2)+" in queue_features")
    '''
    FLAG_STOP=False
    while FLAG_STOP is False:
        data = queue_raw.get()  # get will wait
        if data is None:
            # Finish analysis
            FLAG_STOP = True
        else:
            # work with data
            queue_features.put(data**2)
            print("calcFeatures: put "+ str(data**2)+" in queue_features")

def sendFeatures(queue_features):
    while not queue_features.empty():
        feature = queue_features.get()
        print("sendFeatures: put "+ str(feature)+" out")

if __name__ == "__main__":

    queue_raw = multiprocessing.Queue()
    queue_features = multiprocessing.Queue()

    processes = [

        multiprocessing.Process(target=getData, args=(queue_raw,)),
        multiprocessing.Process(target=calcFeatures, args=(queue_raw, queue_features,)),
        multiprocessing.Process(target=sendFeatures, args=(queue_features,))
    ]

    processes[0].start()
    time.sleep(0.1)
    processes[1].start()
    time.sleep(0.1)
    processes[2].start()

    #for p in processes:
    #    p.start()
    for p in processes:
        p.join()
        
    # https://stackoverflow.com/questions/69972150/python-multiprocessing-how-to-start-processes-that-depend-on-each-other