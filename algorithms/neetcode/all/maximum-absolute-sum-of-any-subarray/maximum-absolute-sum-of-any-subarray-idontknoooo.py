'''
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1479439/python-3-kadanes-algorithm-dp-explanation

Explanation
    Keep track of a lowest value (negative possibly) and highest value
    Use abs to find the maximum absolute subarray sum
Implementation
'''
from typing import List

class S:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = neg = pos = 0
        for num in nums:
            pos = max(pos + num, num)
            neg = min(neg + num, num)
            ans = max(ans, -neg, pos)
        return ans

nums = [1,-3,2,3,-4]
print(S().maxAbsoluteSum(nums))


class Simplified:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        neg = pos = 0
        return max(max(pos:=max(pos + num, num), abs(neg:=min(neg+num, num))) for num in nums)

print(Simplified().maxAbsoluteSum(nums))
