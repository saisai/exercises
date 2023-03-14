
from typing import List

class S:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, 0
        res, total = 0, 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res

nums = [1,2,4]
k = 5
print(S().maxFrequency(nums, k))
