'''

https://leetcode.com/problems/selling-pieces-of-wood/discuss/2176350/python3-dp
https://leetcode.com/problems/selling-pieces-of-wood/
'''
from functools import cache
from typing import List

class S:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:

        mp = { (h, w) : p for h, w, p in prices }

        print(mp)
        @cache
        def fn(m, n):
            """Return max money of a mxn piece of wood."""

            if m == 0 or n == 0: return 0
            ans = 0
            if (m, n) in mp: ans = mp[m, n]
            if m > 1: ans = max(ans, max(fn(i, n) + fn(m-i, n) for i in range(1, m//2+1)))
            if n > 1: ans = max(ans, max(fn(m, j) + fn(m, n-j) for j in range(1, n//2+1)))
            return ans
        return fn(m, n)

m = 3
n = 5 
prices = [[1,4,2],[2,2,7],[2,1,3]]
print(S().sellingWood(m, n, prices))
