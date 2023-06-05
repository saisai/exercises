

class S:
    def numWays(self, steps, arrLen):
        n = min(steps // 2 + 1, arrLen)
        mod = 10 ** 9 + 7
        dp = [1] + [0] * n
        for _ in range(steps):
            prev = 0
            for i in range(n):
                dp[i], prev = (prev + dp[i] + dp[i + 1]) % mod, dp[i]
        return dp[0]

steps = 3
arrLen = 2
print(S().numWays(steps, arrLen))