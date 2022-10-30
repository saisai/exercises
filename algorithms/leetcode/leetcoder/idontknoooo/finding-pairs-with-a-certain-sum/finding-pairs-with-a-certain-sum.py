'''
https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
https://leetcode.com/problems/finding-pairs-with-a-certain-sum/solutions/1327517/python-3-hash-table-explanation/

'''

import collections
from typing import List

class S:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = collections.Counter(nums1)
        self.d2 = collections.defaultdict(int)
        self.cnt2 = collections.defaultdict(int)
        for i, num in enumerate(nums2):
            self.d2[i] = num
            self.cnt2[num] += 1

    def add(self, index: int, val: int) -> None:
        cur = self.d2[index]    # get value by index
        self.cnt2[cur] -= 1     # cnt minus 1
        self.d2[index] += val   # update value
        self.cnt2[cur+val] += 1 # new value cnt plus 1

    def count(self, tot: int) -> int:
        return sum([self.cnt2[tot-val] * l for val, l in self.cnt1.items()])

nums1 = [1, 1, 2, 2, 2, 3]
nums2 = [1, 4, 5, 2, 5, 4]
s = S(nums1, nums2)
print(s.count(7))
s.add(3, 2)
print(s.count(8))
print(s.count(4))
s.add(0, 1)
s.add(1, 1)
print(s.count(7))

