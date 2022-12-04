"""
https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/
https://www.youtube.com/watch?v=LziQ6Qx9sks&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=34&ab_channel=NeetCode

"""

class S:

    def minDays(self, n: int) -> int:

        dp = {0: 0, 1: 1}

        def dfs(n):
            if n in dp:
                return dp[n]

            one = 1 + (n % 2) + dfs(n // 2)
            two = 1 + (n % 3) + dfs(n // 3)
            dp[n] = min(one, two)
            return dp[n]

        return dfs(n)

n = 10
print(S().minDays(n))
