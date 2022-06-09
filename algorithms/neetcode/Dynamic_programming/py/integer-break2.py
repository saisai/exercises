
class S:
    def integerBreak(self, n):
        def dfs(num, t = None):

            dp = { 1 : 1}
            print('t ', t)
            if num in dp:
                return dp[num]
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i, 'left') * dfs(num - i, 'right')
                dp[num] = max(dp[num], val)
            #print('res ', res)
            return dp[num]
        return dfs(n)
n = 2
print(S().integerBreak(n))

