'''
https://www.youtube.com/watch?v=5WZl3MMT0Eg&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=3&ab_channel=NeetCode

https://leetcode.com/problems/maximum-subarray/

'''
from typing import List

class S:

    def maxSubArray(self, nums: List[int]) -> int:

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(S().maxSubArray(nums))
