
class S:
    def integerBreak(self, n):
        def dfs(num, t = None):
            print('t ', t)
            if n == 1:
                return 1
            res = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i, 'left') * dfs(num - i, 'right')
                res = max(res, val)
            print('res ', res)
            return res
        return dfs(n)
n = 2
print(S().integerBreak(n))

