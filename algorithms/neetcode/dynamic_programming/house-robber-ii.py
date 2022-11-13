
from typing import List

class S:
    def rob(self, nums: List[int]) -> int:
    
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):

        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

for nums in [[2,3,2], [1,2,3,1]]:
    print(S().rob(nums))
