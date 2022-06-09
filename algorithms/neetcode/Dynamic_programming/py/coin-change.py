class S:

    def __call__(self, coins, amount):

        dp = [ amount + 1] * (amount + 1)
        print(dp)
        dp[0] = 0

        print(dp)

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a -c ])

        print(dp)
        print(amount)
        return dp[amount] if dp[amount] != amount + 1 else -1


coins = [1,2,5]
amount = 11

print(S()(coins, amount))

coins=[2]
amount = 3
print(S()(coins, amount))
