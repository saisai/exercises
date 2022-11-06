
from typing import List

class S:

    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

for nums in [ [1,2,3,1], [2,7,9,3,1] ]:
    print(S().rob(nums))
