'''
import multiprocessing
from difflib import SequenceMatcher
from uuid import uuid4

# Let's generate a large list with random data
# where we have few duplicates: "abc" indices: 0, 1_001 ; "b" - indices 1_002, 1_003
jsn = ['abc'] + [str(uuid4()) for _ in range(1_000)] + ['abc', 'b', 'b']

def compare_strings(a: int, b: int):
    if ((jsn[a] == jsn[b]) or (SequenceMatcher(None, jsn[a], jsb[b]).ratio() > 40)):
        return a, b

# now we are comparing all possible pairs using multiprocessing
with multiprocessing.Pool(processes=10) as pool:
    results = pool.starmap(compare_strings, [(i, j) for i in range(len(jsn)) for j in range(i +1, len(jsn))])

for result in results:
    if result is not None:
        a, b = result
        print(f"Dulicate pair: {a} {b} {jsn[b]}")
'''

# https://stackoverflow.com/questions/73733109/why-python-thread-and-process-not-working
import multiprocessing
from difflib import SequenceMatcher
from uuid import uuid4

# Let's generate a large list with random data
# where we have few duplicates: "abc" indices: 0, 1_001 ; "b" - indices 1_002, 1_003
jsn = ['abc'] + [str(uuid4()) for _ in range(1_000)] + ['abc', 'b', 'b']


def compare_strings(a: int, b: int):
    if ((jsn[a] == jsn[b]) or (SequenceMatcher(None, jsn[a], jsn[b]).ratio() > 40)):
        return a, b


# now we are comparing all possible pairs using multiprocessing
with multiprocessing.Pool(processes=10) as pool:
    results = pool.starmap(compare_strings, [(i, j) for i in range(len(jsn)) for j in range(i + 1, len(jsn))])

for result in results:
    if result is not None:
        a, b = result
        print(f"Duplicated pair: {a} {b} {jsn[b]}")
        # delete duplicates

