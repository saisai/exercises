"""


https://leetcode.com/problems/soup-servings/
https://leetcode.com/problems/soup-servings/discuss/1651208/python-3-bottom-up-top-down-dp-explanation

Explanation
Observe the probability, you will find a tends to be used up quicker than b
Meaning when n is large enough, the answer will always be 1
4275 is the magic number I tested based on idea above, credit to @anarchaworld
See more explanation in code comments
Top-down
"""

from functools import cache


class S:
    def soupServings(self, n):
        @cache      # cache the result for input (a, b)
        def dfs(a, b):
            if a <= 0 and b > 0: return 1   # set criteria probability
            elif a <= 0 and b <= 0: return 0.5
            elif a > 0 and b <= 0: return 0
            return (dfs(a-4, b) + dfs(a-3, b-1) + dfs(a-2, b-2) + dfs(a-1, b-3)) * 0.25 # dfs
        if n > 4275: return 1       # observe the distribution you will find `a` tends to be easier toget used up than `b`
        n /= 25                 # reduce the input scale
        return dfs(n, n)        # both soup have `n` ml

n = 50
n = 100
print(S().soupServings(n))
