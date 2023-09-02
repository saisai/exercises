import os, random, sys, time, string
import multiprocessing as mp

letters = string.ascii_uppercase
align_len = 1300

SENTINEL = None # no more records sentinel

def return_string():
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

    return alignments


def run_string_gen(cores):
    def my_callback(result):
        alignments = result
        for alignment in alignments:
            print(alignment)

    pool = mp.Pool(cores)
    for i in range(1000):
        pool.apply_async(return_string, callback=my_callback)
    # wait for completion of all tasks:
    pool.close()
    pool.join()

if __name__ == "__main__":
    cores = int(sys.argv[1])
    if cores > os.cpu_count():
        cores = os.cpu_count()
    start = time.perf_counter()
    run_string_gen(cores)
    print(f"it took {time.perf_counter() - start}")
    print('os.cpucounts ', os.cpu_count())
    
    # https://stackoverflow.com/questions/70465276/multiprocessing-hanging-at-join