'''
https://leetcode.com/problems/number-of-excellent-pairs/discuss/2324816/python3-sum-of-set-bits
https://leetcode.com/problems/number-of-excellent-pairs/

'''
from itertools import accumulate
from typing import List

class S:

    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        freq = [0]*30
        for x in nums: freq[bin(x).count('1')] += 1
        prefix = list(accumulate(freq, initial=0))
        ans = 0
        for x in nums:
            bits = bin(x).count('1')
            lo = min(30, max(0, k-bits))
            ans += prefix[-1] - prefix[lo]
        return ans

nums = [1,2,3,1]
k = 3
print(S().countExcellentPairs(nums, k))
