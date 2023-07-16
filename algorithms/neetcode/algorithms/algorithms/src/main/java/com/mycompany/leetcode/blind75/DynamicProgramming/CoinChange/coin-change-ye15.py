
from typing import List
from math import inf

class S:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount
        for x in range(amount):
            if dp[x] < inf:
                for coin in coins:
                    if x + coin <= amount:
                        dp[x + coin] = min(dp[x+coin], 1 + dp[x])
        return dp[-1] if dp[-1] < inf else -1

coins = [1,2,5]
amount = 11
print(S().coinChange(coins, amount))

