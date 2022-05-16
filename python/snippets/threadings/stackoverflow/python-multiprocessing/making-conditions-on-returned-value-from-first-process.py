from multiprocessing import Manager, Process
import time
import ctypes

def test1(a):
    print("\n#######################\nFunction 1")
    time.sleep(1)
    print(a.value)
    a.value = "Loaded Data"

def test2(a):
    print("\n#######################\nFunction 2")
    print(a.value)

if __name__ == '__main__':
    manager = Manager()
    a = manager.Value(ctypes.c_wchar_p, "Wait")

    t1 = Process(target=test1, args=(a,))
    t1.start()
    time.sleep(2)
    t2 = Process(target=test2, args=(a,))
    t2.start()
    t1.join()
    t2.join()
    
    # https://stackoverflow.com/questions/69114139/making-conditions-on-returned-value-from-first-process