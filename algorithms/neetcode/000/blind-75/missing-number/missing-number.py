'''
https://www.youtube.com/watch?v=WnPLSRLSANE&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=14&ab_channel=NeetCode

https://leetcode.com/problems/missing-number/

'''
from typing import List


class S:

    def missingNumber(self, nums: List[int]) -> int:

        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res

nums = [3,0,1]

print(S().missingNumber(nums))
