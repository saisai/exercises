
'''
https://leetcode.com/problems/rotate-function/

https://leetcode.com/problems/rotate-function/solutions/857056/python-3-py38-math-on-explanation/

'''
from typing import List

class S:

    def maxRotateFunction(self, A: List[int]) -> int:
        s, n = sum(A), len(A)
        cur_sum = sum([i*j for i, j in enumerate(A)])
        ans = cur_sum
        for i in range(n): ans = max(ans, cur_sum := cur_sum + s-A[n-1-i]*n)
        return ans

nums = [4,3,2,6]
print(S().maxRotateFunction(nums))
