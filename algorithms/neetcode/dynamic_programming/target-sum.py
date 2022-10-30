'''
https://leetcode.com/problems/target-sum/
https://www.youtube.com/watch?v=g0npyaQtAQM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&ab_channel=NeetCode
'''
from typing import List

class S:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total)
        def backtrack(i, total, name):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            # dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
            #                backtrack(i + 1, total - nums[i]))
            plus = backtrack(i + 1, total + nums[i], "plus" + str(i))
            minus = backtrack(i + 1, total - nums[i], "minus" + str(i))
            dp[(i, total)] = plus + minus
            return dp[(i, total)]
        
        return backtrack(0, 0, "main")
nums = [1,1,1,1,1]
target = 3

nums = [1,1,1,1]
target = 2
print(S().findTargetSumWays(nums, target))
