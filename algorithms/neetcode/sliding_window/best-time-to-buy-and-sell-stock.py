
from typing import List

class S:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left=buy, right=sell
        maxP = 0

        while r < len(prices):
            # profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l += 1
            r += 1

        return maxP

prices = [7,1,5,3,6,4]
print(S().maxProfit(prices))
