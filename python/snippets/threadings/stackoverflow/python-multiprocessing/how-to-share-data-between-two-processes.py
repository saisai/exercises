from multiprocessing import Process, Value

class exp:
    def __init__(self):
        self.var1 = Value('i', 0, lock=False)

    def func1(self):

        self.var1.value = 5
        print(self.var1.value)

    def func2(self):

        print(self.var1.value)


if __name__ == "__main__":

    #multiprocessing
    obj = exp()
    p1 = Process(target = obj.func1)
    p2 = Process(target = obj.func2)

    print("multiprocessing")
    p1.start()
    # No need to sleep, just wait for p1 to complete
    # before starting p2:
    #time.sleep(2)
    p1.join()
    p2.start()
    p2.join()