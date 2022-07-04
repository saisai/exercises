class S:
    
    @staticmethod
    def maxProfit(prices):
        l, r = 0, 1 # left=buy, right=sell
        maxP = 0

        while r < len(prices):
            # profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP

prices = [7,1,5,3,6,4]
print(S.maxProfit(prices))



