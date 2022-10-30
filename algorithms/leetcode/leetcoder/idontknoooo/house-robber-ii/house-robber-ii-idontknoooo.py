'''

https://leetcode.com/problems/house-robber-ii/

https://leetcode.com/problems/house-robber-ii/solutions/894408/python-3-two-pass-one-pass-dp-explanation/

Explanation
    Two situation as hinted, either rob 0 to house n-1 or 1 to house n
    Create 2 array and use two for loop to make this happen
        dp[i] = max(dp[i-1], dp[i-2]+nums[i]) either take the left neighbor only or take the left-left neighbor and add current house's value
    Use ans to keep track of maximum
Implementation
'''
from typing import List

class S:

    def rob(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0] * n
        for i in range(n-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            ans = max(ans, dp[i])
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])
            ans = max(ans, dp[i])
        return ans

nums = [2,3,2]
print(S().rob(nums))

