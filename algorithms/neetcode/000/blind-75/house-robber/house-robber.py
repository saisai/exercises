'''
https://leetcode.com/problems/house-robber/
https://www.youtube.com/watch?v=73r3KWiEvyk&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=21&ab_channel=NeetCode

'''
from typing import List

class S:

    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

nums = [1,2,3,1]
print(S().rob(nums))
