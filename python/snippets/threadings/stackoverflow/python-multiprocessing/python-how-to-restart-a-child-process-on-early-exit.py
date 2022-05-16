from multiprocessing import Pool
from time import sleep

def foo():
    print("foo here")
    sleep(3)
    raise Exception

def bar():
    print("bar here")
    while True:
        sleep(5)
        print("'bar'-process still alive")

if __name__ == "__main__":
    restarts = foo, bar
    results = {func: None for func in restarts}
    with Pool(processes=2) as p:
        while True:
            for func in restarts:
                results[func] = p.apply_async(func)
                print(f"'{func.__name__}'-process (re)started")
            sleep(1)
            restarts = (
                func
                for func, result in results.items()
                if result.ready() and not result.successful()
            )
    # https://stackoverflow.com/questions/69025763/python-how-to-restart-a-child-process-on-early-exit