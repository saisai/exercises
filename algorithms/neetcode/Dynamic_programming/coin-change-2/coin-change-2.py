'''
https://www.youtube.com/watch?v=Mjy4hd2xgrs&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=5&ab_channel=NeetCode
https://leetcode.com/problems/coin-change-2/

'''
from typing import List

class S:
    def change(self, amount: int, coins: List[int]) -> int:


        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) -1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]

        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]


        cache = {}
        def dfs(i, a):
            if a == amount:
                return 1
            if a >= amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]
        return dfs(0, 0)
amount = 5
coins = [1,2,5]
print(S().change(amount, coins))

