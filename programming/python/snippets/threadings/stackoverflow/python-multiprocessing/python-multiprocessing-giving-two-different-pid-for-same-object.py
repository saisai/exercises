import multiprocessing
import os

class BaseModule:
    def __init__(self):
        print("Initialize time pid: ",os.getpid())

    def get_pid(self):
        print("After new process pid: ",os.getpid())

    def run(self):
        self.get_pid()

def use_multiprocessing():
    obj = BaseModule()
    obj.run()

if __name__ == '__main__':
    process = multiprocessing.Process(target=use_multiprocessing)
    process.start()
    
    # https://stackoverflow.com/questions/70228892/python-multiprocessing-giving-two-different-pid-for-same-object