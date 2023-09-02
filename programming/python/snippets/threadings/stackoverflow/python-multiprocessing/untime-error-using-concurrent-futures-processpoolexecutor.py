from multiprocessing import freeze_support
import concurrent.futures

class Objects(object):

    def __init__(self, var1=1, var2=2):
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            executor.map(self.function_for_multiprocess, (var1, var2))

    def function_for_multiprocess(var1, var2):
        print('var1:', var1)
        print('var2:', var2)

def abc(x):
    return x

def main():
    print('abc:', abc(200))

if __name__ == "__main__":
    #freeze_support()
    obj = Objects(5, 10)
    main()
    # https://stackoverflow.com/questions/70397431/runtime-error-using-concurrent-futures-processpoolexecutor