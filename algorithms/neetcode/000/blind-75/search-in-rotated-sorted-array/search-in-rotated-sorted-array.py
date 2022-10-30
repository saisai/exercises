'''
https://www.youtube.com/watch?v=U8XENwh8Oy8&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=8&ab_channel=NeetCode
https://leetcode.com/problems/search-in-rotated-sorted-array/
'''
from typing import List

class S:

    @staticmethod
    def search(nums: List[int], target: int) -> int:

        print('test')
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r ) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(S().search(nums, target))
