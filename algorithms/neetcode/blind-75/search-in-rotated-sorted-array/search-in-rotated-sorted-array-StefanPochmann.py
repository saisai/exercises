
'''
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14419/Pretty-short-C%2B%2BJavaRubyPython
https://leetcode.com/problems/search-in-rotated-sorted-array/
'''
from typing import List

class S:

    @staticmethod
    def search(nums: List[int], target: int) -> int:

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo+1] else -1


nums = [4,5,6,7,0,1,2]
target = 0
print(S().search(nums, target))
