
class S:
    def rob(self, nums):
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)
        return dp2

nums = [1,2,3,1]
print(S().rob(nums))
