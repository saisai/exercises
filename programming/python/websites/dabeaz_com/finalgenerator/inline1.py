
class Task:

    def __init__(self, gen):
        self.__gen = gen

    def step(self, value=None):
        try:
            fut = self.__gen.send(value)
            fut.add_done_callback(self._wakeup)
        except StopIteration as e:
            pass

    def _wakeup(self, fut):
        result = fut.result()
        self.step(result)


if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor
    import time

    pool = ThreadPoolExecutor(max_workers=8)

    def func(x, y):
        time.sleep(1)
        return x + y

    def do_func(x, y):
        result = yield pool.submit(func, x, y)
        print("Got:", result)

    t = Task(do_func(2, 3))
    t.step()


    # Example of a function that makes repeated reqeusts to the pool
    def do_many(n):
        while n > 0:
            result = yield pool.submit(func, n, n)
            print("Got :", result)
            n -= 1

    t2 = Task(do_many(10))
    t2.step()

