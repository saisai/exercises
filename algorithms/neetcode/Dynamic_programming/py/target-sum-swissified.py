'''
https://leetcode.com/problems/target-sum/discuss/1198338/Python-recursive-solution-with-memoization-(DFS)
https://leetcode.com/problems/target-sum/
'''
from collections import defaultdict

class S:
    def findTargetSumWays(self, nums, target):

        dic = defaultdict(int)

        def dfs(index=0, total=0):
            key = (index, total)

            if key not in dic:
                if index == len(nums):
                    return 1 if total == target else 0
                else:
                    dic[key] = dfs(index+1, total+nums[index]) + dfs(index+1, total-nums[index])
            return dic[key]

        return dfs()

nums = [1,1,1,1,1]
target = 3
print(S().findTargetSumWays(nums, target))
