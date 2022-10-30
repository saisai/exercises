'''
https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&ab_channel=NeetCode

https://leetcode.com/problems/two-sum/
'''

from typing import List

class S:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} # val: index

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
nums = [2,7,11,15]
target = 9
print(S().twoSum(nums, target))
