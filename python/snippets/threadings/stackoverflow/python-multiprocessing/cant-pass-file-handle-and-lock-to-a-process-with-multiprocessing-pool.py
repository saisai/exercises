import multiprocessing as mp
import time
import random

resultq = mp.Queue()


def thr_work00(args):
    global resultq
    s = random.randint(0, 5)
    print(f"\x1b[92m{args[0]} \x1b[32m{s}\x1b[0m")
    time.sleep(s)
    resultq.put((args[0], s))
    return args


def thr_writer():
    global resultq
    print('writer start')
    with open('test.txt', 'w') as fd:
        while True:
            item = resultq.get()
            if item is None:
                break
            fd.write(f'{item[0]}: {item[1]}\n')
    print('writer exit')

if __name__ == '__main__':
    
    with open("test.txt", "w") as o_file:
        o_lock = mp.Lock()

        writer = mp.Process(target=thr_writer)
        writer.start()

        tasks = [
            [0, 0, 1],
            [1, 2, 3],
            [2, 4, 5],
            [3, 6, 7],
        ]

        with mp.Pool(2) as pool:
            results = pool.map(thr_work00, tasks)
            for res in results:
                print(res)

        resultq.put(None)
        writer.join()