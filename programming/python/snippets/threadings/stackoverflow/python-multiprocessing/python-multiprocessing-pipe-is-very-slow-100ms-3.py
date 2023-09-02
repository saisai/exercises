import multiprocessing as mp
import time

def proc(child_conn):
    for i in range(5):
        child_conn.recv()
        ts = time.time_ns()
        child_conn.send(ts)

if __name__ == "__main__":

    parent_conn, child_conn = mp.Pipe()
    p1 = mp.Process(target=proc, args=(child_conn,))
    p1.start()

    for i in range(5):
        ts = time.time_ns()
        parent_conn.send("START")
        ts_end = parent_conn.recv()

        print(f"Time taken in ms: {(ts_end - ts)/(10**6)}")

    # https://stackoverflow.com/questions/70784547/python-multiprocessing-pipe-is-very-slow-100ms