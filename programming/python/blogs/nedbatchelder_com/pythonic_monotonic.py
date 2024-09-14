
import itertools

def mono_runs_pythonic(seq):

    class Monotonic:
        def __init__(self):
            self._last = float("-inf")

        def __call__(self, curr):
            res = curr < self._last
            self._last = curr
            return res

    return [
        list(group)[::-1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(seq, Monotonic())
    ]

result = mono_runs_pythonic([1, 2, 3, 2, 1, 4, 5, 6, 7])
print(result)

 # https://nedbatchelder.com/blog/202108/pythonic_monotonic.html
