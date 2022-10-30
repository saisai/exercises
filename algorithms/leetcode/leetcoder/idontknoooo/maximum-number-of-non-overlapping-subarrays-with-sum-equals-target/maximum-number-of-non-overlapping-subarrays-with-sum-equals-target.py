'''
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/solutions/781243/python-3-prefix-sum-and-non-overlapping-intervals/
'''
from typing import List
import collections
import sys

class S:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        d = collections.defaultdict(int)
        print(d)
        d[0] = -1
        print(d)
        cur, intervals = 0, []
        for i, num in enumerate(nums):
            cur += num
            if cur - target in d:
                intervals.append([d[cur-target]+1, i])
            d[cur] = i

        n = len(intervals)
        end, erased = -sys.maxsize, 0
        for i in intervals:
            if i[0] > end: end = i[1]
            else: erased += 1
        return n - erased


nums = [1,1,1,1,1]
target = 2
print(S().maxNonOverlapping(nums, target))

