'''
https://www.youtube.com/watch?v=g0npyaQtAQM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&ab_channel=NeetCode
https://leetcode.com/problems/target-sum/
'''
class S:
    def findTargetSumWays(self, nums, target):
        dp = {} # (index, total) -> # of ways
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i+ 1, total - nums[i]))
            return dp[(i, total)]
        return backtrack(0, 0)
nums = [1,1,1,1,1]
target = 3
print(S().findTargetSumWays(nums, target))
