'''
https://leetcode.com/problems/product-of-array-except-self/discuss/409640/Python-O(n)-constant-space-(with-two-pointers-and-simple)
https://leetcode.com/problems/product-of-array-except-self/

'''
from typing import List

class S:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # output array (just fill emptywith 1s)
        res = [1] * len(nums)

        # left and right pointers
        lo = 0
        hi = len(nums) - 1
        # product for left and right
        leftProduct = 1
        rightProduct = 1
        # keep going until pointers meet
        while lo < len(nums):
            # add running from the l/r products to these spots
            res[lo] *= leftProduct
            res[hi] *= rightProduct
            # multiply products by current in nums
            rightProduct *= nums[hi]
            leftProduct *= nums[lo]
            # inc/dec pointers
            lo += 1
            hi -= 1
        return res


nums = [1,2,3,4]
print(S().productExceptSelf(nums))
