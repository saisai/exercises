'''
https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/discuss/2176348/python3-dp-math
https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

'''
from functools import cache
from math import inf

class S:
    def minimumNumbers(self, num: int, k: int) -> int:

        # math
        if num == 0: return 0
        for x in range(1, 11):
            if x*k <= num and (num - x*k) % 10 == 0: return x
        return -1
        # DP
        @cache
        def fn(x):
            """Return min size for x."""
            if x == 0: return 0
            ans = inf
            for cand in range(1, x+1):
                if cand % 10 == k: ans = min(ans, 1 + fn(x-cand))
            return ans

        ans = fn(num)
        return ans if ans < inf else -1

num = 58
k = 9
print(S().minimumNumbers(num, k))
