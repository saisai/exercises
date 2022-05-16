
class S:

    def __call__(self, nums):

        dp = [0 for _ in nums]
        print(dp)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(S()(nums))
# https://leetcode.com/problems/maximum-subarray/discuss/1960595/Very-easy-to-understand-O(n)-simplified-Kadane's-algorithm.
