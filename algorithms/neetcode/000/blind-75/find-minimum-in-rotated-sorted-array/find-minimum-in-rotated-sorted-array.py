'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
https://www.youtube.com/watch?v=nIVW4P8b1VA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=7&ab_channel=NeetCode

'''
from typing import List

class S:
    
    @classmethod
    def findMin(cls, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r ) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

nums = [3,4,5,1,2]
print(S.findMin(nums))
