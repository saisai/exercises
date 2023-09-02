def process(idx, in_q, out_q):
    while True:
        task = in_q.get()
        if task is None:
            break
        out_q.put({'n': task['n'] + 1})

def main():
    import multiprocessing, time

    queue_size = 1 << 16
    procs = []
    for i in range(multiprocessing.cpu_count()):
        in_q, out_q = [multiprocessing.Queue(queue_size) for j in range(2)]
        procs.append({
            'in_q': in_q,
            'out_q': out_q,
            'proc': multiprocessing.Process(target = process,
                kwargs = dict(idx = i, in_q = in_q, out_q = out_q)),
        })
        procs[-1]['proc'].start()

    num_blocks = 1 << 2
    block = 1 << 10
    assert block <= queue_size

    tb = time.time()
    for k in range(num_blocks):
        # Send tasks
        for i in range(block):
            for j, proc in enumerate(procs):
                proc['in_q'].put({'n': k * block * len(procs) + i * len(procs) + j})
        # Receive tasks results
        for i in range(block):
            for proc in procs:
                proc['out_q'].get()
    print('Processing speed:', round((time.time() - tb) /
        (num_blocks * block * len(procs)) * 1_000_000, 1), 'mcs per task')
    
    # Send finish signals to processes
    for proc in procs:
        proc['in_q'].put(None)
    # Join processes (wait for exit)
    for proc in procs:
        proc['proc'].join()

if __name__ == '__main__':
    main()