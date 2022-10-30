"""

https://leetcode.com/problems/rle-iterator/
https://leetcode.com/problems/rle-iterator/solutions/1311888/python-3-java-deque-explanation/
"""
from typing import List
import collections

class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.q = collections.deque(encoding)

    def next(self, n: int) -> int:
        while self.q and n >= self.q[0]:
            n -= self.q[0]
            self.q.popleft()
            self.q.popleft()

        if self.q and n <= self.q[0]:
            self.q[0] -= n
            return self.q[1]
        return -1

encoding = [3, 8, 0, 9, 2, 5]
obj = RLEIterator(encoding)
print(obj.next(2))
print(obj.next(1))
print(obj.next(1))
print(obj.next(2))


