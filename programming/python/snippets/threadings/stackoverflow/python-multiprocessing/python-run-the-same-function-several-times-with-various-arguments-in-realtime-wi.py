import threading
import ctypes

def func(*args, **kwArg):
    func2(f)

def func2(f):
    ctypes.windll.user32.MessageBoxW(0, f, "Title", 0)

if __name__ == '__main__':
    threads = []

    fruits = ['apple', 'banana', 'cherry']
    for f in fruits:
        t = threading.Thread(target=func, args=(f))  
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        
    # https://stackoverflow.com/questions/69558786/python-run-the-same-function-several-times-with-various-arguments-in-realtime-wi