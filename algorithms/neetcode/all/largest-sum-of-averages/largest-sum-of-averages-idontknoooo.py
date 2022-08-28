'''
https://leetcode.com/problems/largest-sum-of-averages/
https://leetcode.com/problems/largest-sum-of-averages/discuss/1490536/python-3-dp-explanation

Explanation
    dp[i][k] meaning the maximum sum of averages for nums[:i] spliting in k parts
    dp[i][k] = max((dp[j][k-1] + avg(i, j)) for each j < i)
        This means, we can try out all possible match of k-1 splits, and take the maximum
Use prefix array to help find average

Implementation
'''

from typing import List

class S:

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:

        pre_sum = [0]
        for num in nums: pre_sum.append(pre_sum[-1] + num)
        avg = lambda i, j: (pre_sum[i+1] - pre_sum[j+1]) / (i-j)
        print(avg)
        print(pre_sum)

        n = len(nums)
        dp = [[0] * k for _ in range(n)]
        for i in range(n): dp[i][0] = pre_sum[i+1] / (i+1)
        print(dp)

        for i in range(1, n):
            for kk in range(1, k):
                for j in range(kk-1, i):
                    dp[i][kk] = max(dp[i][kk], dp[j][kk-1] + avg(i, j))
        return dp[n-1][k-1]

nums = [9,1,2,3,9]
k = 3

print(S().largestSumOfAverages(nums, k))

