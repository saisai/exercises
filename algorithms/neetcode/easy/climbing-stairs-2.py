
class S:

    def climbStairs(self, n):
        
        cache = {}
        def rec(i):
            if i in cache: return  cache[i]
            if i <= 2: return i
            cache[i] = rec(i - 1) + rec(i - 2)
            return cache[i]
        
        return rec(n)

n = 3

print(S().climbStairs(n))

