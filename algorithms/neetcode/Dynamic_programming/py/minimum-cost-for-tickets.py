
class S:

    def __call__(self, days, costs):
        dp = {}
        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = float('inf')
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]
        return dfs(0)
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(S()(days, costs))
