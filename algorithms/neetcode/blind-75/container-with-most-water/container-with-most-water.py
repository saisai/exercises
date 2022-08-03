'''
https://leetcode.com/problems/container-with-most-water/
https://www.youtube.com/watch?v=UuiTKBwPgAo&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=10&ab_channel=NeetCode

'''
from typing import List
class S:


    def maxArea(self, height: List[int]) -> int:
        # Time complexity: O(n)

        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = ( r - l ) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

        # brute force

        # O(n^2)

        res = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r -l) * min(height[l], height[r])
                res = max(res, area)
        return res

height = [1,8,6,2,5,4,8,3,7]
print(S().maxArea(height))

