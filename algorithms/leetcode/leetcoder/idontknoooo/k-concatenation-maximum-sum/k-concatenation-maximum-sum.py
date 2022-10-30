
'''

https://leetcode.com/problems/k-concatenation-maximum-sum/

https://leetcode.com/problems/k-concatenation-maximum-sum/solutions/382897/clean-python-code-with-explaination/

    # left: max starting from index 0 (from left)
    # s: sum(arr)
    # m: max subarray (start anywhere)
    # right: max starting from the right
	# result = left + max(0, s) * (k-2) + right
    # or     = m
    #        e.g. [-3,-2, 5, -1] * 2

'''
from typing import List

class S:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        left = cur = s = m = 0
        for num in arr:
            s += num
            left = max(left, s)

            cur += num
            m = max(m, cur)
            cur = 0 if cur < 0 else cur

        right = cur = 0
        for num in arr[::-1]:
            cur += num
            right = max(right, cur)

        middle = max(s, 0) * (k - 2)
        return max(m, (left + middle + right)) % (10**9 + 7)

arr = [1,2]
k = 1
print(S().kConcatenationMaxSum(arr, k))
