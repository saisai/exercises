"""
This is also built-in to the standard library:

"""

import bisect
def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        bisect.insort(seq, seq.pop(i), 0, i)

seq = [4, 65, 2, -31, 0, 99, 83, 782, 1]
insertion_sort_bin(seq)
print(seq)
