'''
https://leetcode.com/problems/arithmetic-slices/
https://leetcode.com/problems/arithmetic-slices/solutions/824441/python-3-dp-math-explanation/

'''
import sys
from typing import List

class S:

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        diff = [0] * (n-1)
        for i, val in enumerate(zip(A, A[1:])): diff[i] = val[1] - val[0]       # calculate difference
        diff.append(sys.maxsize)
        as_count, cur = [], 2
        for i in range(1, n):                       # count arithematic sequence and save to as_count
            if diff[i] == diff[i-1]: cur += 1
            else:
                if cur >= 3: as_count.append(cur)
                cur = 2
        return sum((1+cnt-2) * (cnt-2) // 2 for cnt in as_count)    # Use math to add up all arithmatic sequence

nums = [1,2,3,4]
print(S().numberOfArithmeticSlices(nums))

