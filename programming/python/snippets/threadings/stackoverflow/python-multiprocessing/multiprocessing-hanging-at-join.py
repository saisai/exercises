import os, random, sys, time, string
import multiprocessing as mp

letters = string.ascii_uppercase
align_len = 1300

SENTINEL = None # no more records sentinel

def return_string(queue):
    n_strings = [1,2,3,4]
    alignments = []

    # generating 1 to 4 sequences randomly, each sequence of length 1300
    # the original code might even produce more than 4, but 1 to 4 is an average case
    # instead of the random string there will be some complicated function called
    # in the original code
    for i in range(random.choice(n_strings)):
        alignment = ""
        for i in range(align_len):
            alignment += random.choice(letters)
        alignments.append(alignment)

    for a in alignments:
        queue.put(a)
    # show this process is through writing records:
    queue.put(SENTINEL)


def run_string_gen(cores):
    processes = []
    queue = mp.Queue()
    # running the target function 1000 time
    for i in range(1000):
        # print(i)
        process = mp.Process(target=return_string, args = (queue,))
        processes.append(process)
        if len(processes) == cores:
            counter = len(processes)
            for p in processes:
                p.start()

            seen_sentinel_count = 0
            while seen_sentinel_count < len(processes):
                a = queue.get()
                if a is SENTINEL:
                    seen_sentinel_count += 1
                # the original idea is that instead of print
                # I will be writing to a file that is already open
                else:
                    print(a)

            for p in processes:
                p.join()

            processes = []
            # The same queue can be reused:
            #queue = mp.Queue()

    # any leftovers processes
    if processes:
        for p in processes:
            p.start()

        seen_sentinel_count = 0
        while seen_sentinel_count < len(processes):
            a = queue.get()
            if a is SENTINEL:
                seen_sentinel_count += 1
            else:
                print(a)

        for p in processes:
            p.join()

if __name__ == "__main__":
    cores = int(sys.argv[1])
    if cores > os.cpu_count():
        cores = os.cpu_count()
    start = time.perf_counter()
    run_string_gen(cores)
    print(f"it took {time.perf_counter() - start}")
    
    # https://stackoverflow.com/questions/70465276/multiprocessing-hanging-at-join