from multiprocessing import Process, Manager, Lock
from time import sleep
import random
from abc import ABC, abstractmethod


class Trade:
    def __init__(self, id):
        self.exchange = None
        self.order_id = id


class TestProcess(ABC):
    def __init__(self, trades, lock):
        self.trades = trades
        self.lock = lock

    @abstractmethod
    def process():
        pass

class TestProcess2(TestProcess):
    def process(self):
        while True:
            # lock.acquire()
            print("Altering")
            for idx in range(len(self.trades)):
                trade = self.trades[idx]
                trade.order_id = 0
                # We must tell the managed list that it has been updated!!!:
                self.trades[idx] = trade
            # lock.release()
            sleep(1)


class TestProcess1(TestProcess):
    def process(self):
        while True:
            print("start")
            for idx in range(len(self.trades)):
                print(f'index = {idx}, order id = {self.trades[idx].order_id}')

            sleep(1)


class TestProcess(TestProcess):
    def process(self):
        while True:
            # lock.acquire()
            n = random.randint(0, 9)
            print("adding random {}".format(n))
            self.trades.append(Trade(n))
            # lock.release()
            # print(trades)
            sleep(5)


if __name__ == "__main__":

    with Manager() as manager:
        records = manager.list([Trade(5)])
        lock = Lock()

        tp = TestProcess(records, lock)
        p1 = Process(target=tp.process, daemon=True)
        p1.start()

        tp1 = TestProcess1(records, lock)
        p2 = Process(target=tp1.process, daemon=True)
        p2.start()

        tp2 = TestProcess2(records, lock)
        p3 = Process(target=tp2.process, daemon=True)
        p3.start()

        sleep(15)  # run for 15 seconds


        # Using classes not derived from multiprocessing.Process
        # https://stackoverflow.com/questions/71191820/changing-values-of-list-in-multiprocessing
