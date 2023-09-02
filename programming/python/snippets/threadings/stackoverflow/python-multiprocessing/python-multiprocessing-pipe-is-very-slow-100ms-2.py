import multiprocessing as mp
import time

def proc(inp_q, out_q):
    for i in range(5):
        e = inp_q.get()
        ts = float(time.time_ns())
        out_q.put(ts)

if __name__ == "__main__":

    inp_q, out_q = [mp.Queue(1 << 10) for i in range(2)]
    p1 = mp.Process(target=proc, args=(inp_q, out_q))
    p1.start()

    for i in range(5):
        ts = float(time.time_ns())
        inp_q.put("START")
        ts_end = out_q.get()

        print(f"Time taken in ms: {(ts_end - ts)/(10**6)}")
    p1.join()

    # https://stackoverflow.com/questions/70784547/python-multiprocessing-pipe-is-very-slow-100ms