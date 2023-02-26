
from typing import List

class S:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Log(n)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l

nums = [1,3,5,6]
target = 5
print(S().searchInsert(nums, target))
