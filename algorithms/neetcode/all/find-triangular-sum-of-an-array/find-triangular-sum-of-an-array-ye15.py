'''
https://leetcode.com/problems/find-triangular-sum-of-an-array/discuss/2244074/python3-pascals-triangle
https://leetcode.com/problems/find-triangular-sum-of-an-array/

'''
from typing import List

class S:

    def triangularSum(self, nums: List[int]) -> int:

        comb = [1]
        for i in range(len(nums) - 1):
            comb.append(comb[-1] * (len(nums) - 1 - i) // ( i + 1))
        return sum(x * y for x, y in zip(nums, comb)) % 10

nums = [1,2,3,4,5]
print(S().triangularSum(nums))
