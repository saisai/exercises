
class S:
    @classmethod
    def maxProfit(cls, ls):
        lissf = ls[0]
        profit = 0
        for i in range(1, len(ls)):
            if ls[i] > lissf:
                profit = max(profit, ls[i] - lissf)
            else:
                lissf = ls[i]
        return profit
prices = [7,1,5,3,6,4]
print(S.maxProfit(prices))

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1961899/Simplest-Python-Solution

