'''

https://www.youtube.com/watch?v=bNvIQI2wAjk&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=4&ab_channel=NeetCode
https://leetcode.com/problems/product-of-array-except-self/

'''
from typing import List

class S:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

nums = [1,2,3,4]
print(S().productExceptSelf(nums))
