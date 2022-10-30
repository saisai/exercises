'''
https://www.youtube.com/watch?v=RyBM56RIWrM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=12&ab_channel=NeetCode

https://leetcode.com/problems/counting-bits/

'''

from typing import List

class S:

    def countBits(self, n: int) -> List[int]:
        dp = [0] * ( n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

n = 5
print(S().countBits(5))
