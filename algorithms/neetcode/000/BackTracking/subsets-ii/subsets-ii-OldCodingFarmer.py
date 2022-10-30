'''


https://leetcode.com/problems/subsets-ii/
https://leetcode.com/problems/subsets-ii/discuss/30305/Simple-python-solution-(DFS).

'''
class S:
    def subsetsWithDup(self, nums):

        res = []
        nums.sort()

        def dfs(nums, path):
            res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], path+ [nums[i]])
        dfs(nums, [])
        return res

nums = [1,2,2]
print(S().subsetsWithDup(nums))
