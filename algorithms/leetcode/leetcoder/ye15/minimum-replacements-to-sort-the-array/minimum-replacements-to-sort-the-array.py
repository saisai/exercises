from math import ceil
from typing import List

class S:

    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        prev = 1_000_000_001
        for x in reversed(nums):
            d = ceil(x/prev)
            ans += d - 1
            prev = x//d
        return ans
nums = [3,9,3]
print(S().minimumReplacement(nums))
