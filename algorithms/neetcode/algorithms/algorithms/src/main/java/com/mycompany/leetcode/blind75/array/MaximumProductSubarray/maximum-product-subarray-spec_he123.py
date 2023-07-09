
from typing import List

class S:
    def maxProduct(self, nums: List[int]) -> int:
        B = nums[::-1]
        
        for x in range(1, len(nums)):
            if nums[x - 1] != 0:
                nums[x] *= nums[x - 1]
            
            if B[x - 1] != 0:
                B[x] *= B[x - 1]
        return max(nums + B)

nums = [2,3,-2,4]
print(S().maxProduct(nums))