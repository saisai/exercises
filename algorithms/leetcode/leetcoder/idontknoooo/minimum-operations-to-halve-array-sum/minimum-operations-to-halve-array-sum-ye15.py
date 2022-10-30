
'''
https://leetcode.com/problems/minimum-operations-to-halve-array-sum/discuss/1874873/python3-priority-queue
https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
'''
from heapq import *
from typing import List

class S:
    def halveArray(self, nums: List[int]) -> int:
        pq = [-x for x in nums]
        heapify(pq)
        sm = ss = sum(nums)
        ans = 0
        while sm > ss / 2:
            ans += 1
            x = heappop(pq)
            sm -= -x / 2
            heappush(pq, x/2)
        return ans
nums = [5,19,8,1]
print(S().halveArray(nums))
