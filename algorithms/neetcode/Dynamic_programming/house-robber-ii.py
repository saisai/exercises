
class S:

    def __call__(self, nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

class SS:

    def __call__(self, nums):
        if len(nums) == 1:
            return nums[0]
        def rob(nums):
            dp = [0] * (len(nums) + 1)
            dp[0] = 0
            dp[1] = nums[0]
            for i in range(1, len(nums)):
                dp[i+1] = max(dp[i], dp[i-1] + nums[i])
            return dp[len(nums)]
        a = rob(nums[1:])
        b = rob(nums[:-1])
        return max(a, b)

nums = [2,3,2]
print(SS()(nums))
