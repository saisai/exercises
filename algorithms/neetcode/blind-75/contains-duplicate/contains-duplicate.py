
'''
https://leetcode.com/problems/contains-duplicate/
https://www.youtube.com/watch?v=3OamzN90kPg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=3&ab_channel=NeetCode
'''
from typing import List

class S:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

nums = [1,1,1,3,3,4,3,2,4,2]

print(S().containsDuplicate(nums))
