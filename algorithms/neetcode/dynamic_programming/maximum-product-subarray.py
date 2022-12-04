
from typing import List

class S:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:

            curMax = max(curMax * n, curMin * n, n)
            curMin = min(curMin * n, curMin * n, n)
            print(curMax, curMin)
            res = max(res, curMax)

        return res
for nums in [ [2,3,-2,4],
        [-2,0,-1] ]:
    print(S().maxProduct(nums))
