'''

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=2&ab_channel=NeetCode
'''

from typing import List

class S:

    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

prices = [7,1,5,3,6,4]
print(S().maxProfit(prices))
