"""


https://leetcode.com/problems/soup-servings/
https://leetcode.com/problems/soup-servings/discuss/1651208/python-3-bottom-up-top-down-dp-explanation

Explanation
Observe the probability, you will find a tends to be used up quicker than b
Meaning when n is large enough, the answer will always be 1
4275 is the magic number I tested based on idea above, credit to @anarchaworld
See more explanation in code comments
Bottom-up
"""

from functools import cache


class S:
    def soupServings(self, n):
        if n > 4275: return 1       # handle special  case
        n = n // 25 + (n%25 > 0)    # count size of tabulation
        dp = [[0] * (n+1) for _ in range(n+1)]      
        dp[n][n] = 1
        for i in range(n, 0, -1):       # starting from (n, n) for each soup
            for j in range(n, 0, -1):
                for a, b in [[4, 0], [3, 1], [2, 2], [1, 3]]:
                    dp[max(0, i-a)][max(0, j-b)] += dp[i][j] * 0.25 # traverse backwards from(n, n) to (0, 0)
        ans = dp[0][0] / 2          # half the probability when `a` & `b` both tuse up at the same time
        for j in range(1, n + 1):   # plus when `a` use up first
            ans += dp[0][j]
        return ans

n = 50
n = 100
print(S().soupServings(n))
