import time
import multiprocessing as mp

def timer(exit_event):
    for s in range(20):
        if exit_event.is_set():
            print("Yes")
            break
        else:
            time.sleep(1) # if not then continue timing
            
def waiting(exit_event):
    # maybe it waits for an input or a message from "discord or whatsapp"
    time.sleep(5)
    exit_event.set()

if __name__ == '__main__':
    exit_event = mp.Event()
    p1 = mp.Process(target=timer, args=(exit_event,))
    p2 = mp.Process(target=waiting, args=(exit_event,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    # https://stackoverflow.com/questions/70221690/running-two-function-together-with-multiprocessing-and-share-variables