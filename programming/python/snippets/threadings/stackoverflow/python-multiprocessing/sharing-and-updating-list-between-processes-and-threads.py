from multiprocessing import Process, Manager
import time
import threading

def main_thread(l):
    while True:
        l[0][5] += 1
        print("main_thread:", l)
        time.sleep(6)

def sub_thread(l):
    while True:
        l[1][5] += 1
        print("sub_thread:", l)
        time.sleep(7)

def sub_process(l):
    #create a sub_thread to update l[1][5]
    trading_thread = threading.Thread(target=sub_thread, args=(l,))
    trading_thread.start()
    time.sleep(1)
    while True:
        l[0][6] += 1
        print("sub_process:", l)
        time.sleep(9)

def main_process():
    #create a thread to increment l[0][5]
    trading_thread = threading.Thread(target=main_thread, args=(l,))
    trading_thread.start()
    time.sleep(1)
    #Create a sub_process to start a sub_process and increment l[0][6]
    p = Process(target=sub_process, args=(l,))
    p.start()
    time.sleep(1)
    #I need this while loop to run as well:
    while True:
        l[0][7] += 1
        print("main_process: ", l)
        time.sleep(8)
    p.join()    #this could be a problem - we never get to this because sub process is never supposed to finish,
                #I tried to put this before the 'While' loop above but then the loop never gets triggered.

if __name__ == '__main__':
    manager = Manager()
    l = manager.list(
        [['LACE', 1639144800000, 1.157857245, '9:00 December 10, 2021', 'True', 0, 0, 0],
        ['ARKER', 1639109835404, 0.0, '10:00 December 10, 2021', 'True', 0, 0, 0]]
    )
    main_process()
    
    # https://stackoverflow.com/questions/70329433/sharing-and-updating-list-between-processes-and-threads