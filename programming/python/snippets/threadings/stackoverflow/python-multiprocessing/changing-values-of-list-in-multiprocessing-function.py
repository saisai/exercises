from multiprocessing import Process, Manager, Lock
from time import sleep
import random


class Trade:
    def __init__(self, id):
        self.exchange = None
        self.order_id = id


def testprocess2(trades, lock):
    while True:
        # lock.acquire()
        print("Altering")
        for idx in range(len(trades)):
            trade = trades[idx]
            trade.order_id = 0
            # We must tell the managed list that it has been updated!!!:
            trades[idx] = trade
        # lock.release()
        sleep(1)


def testprocess1(trades, lock):
    while True:
        print("start")
        for idx in range(len(trades)):
            print(f'index = {idx}, order id = {trades[idx].order_id}')

        sleep(1)


def testprocess(trades, lock):
    while True:
        # lock.acquire()
        n = random.randint(0, 9)
        print("adding random {}".format(n))
        trades.append(Trade(n))
        # lock.release()
        # print(trades)
        sleep(5)


if __name__ == "__main__":

    with Manager() as manager:
        records = manager.list([Trade(5)])
        lock = Lock()

        p1 = Process(target=testprocess, args=(records, lock), daemon=True)
        p1.start()

        p2 = Process(target=testprocess1, args=(records, lock), daemon=True)
        p2.start()

        p3 = Process(target=testprocess2, args=(records, lock), daemon=True)
        p3.start()

        sleep(15) # run for 15 seconds

        # https://stackoverflow.com/questions/71191820/changing-values-of-list-in-multiprocessing