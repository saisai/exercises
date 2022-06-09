
class S:

    def deleteAndEarn(self, nums):

        max_val = max(nums)

        dp = [0] * (max_val + 1)
        for i in nums:
            dp[i] += i

        print(dp)


        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i] + dp[i-2])
        print(dp)
        return dp[max_val]

nums = [2,2,3,3,3,4]
print(S().deleteAndEarn(nums))

# https://leetcode.com/problems/delete-and-earn/discuss/1941502/Python3-oror-Bottom-Up-Solution
