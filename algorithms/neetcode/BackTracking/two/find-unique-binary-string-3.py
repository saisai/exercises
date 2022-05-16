
class S:

    def findDifferentBinaryString(self, nums):

        self.ans, n = '', len(nums[0])

        def dfs(cur_str):
            if self.ans:
                return
            if len(cur_str) == n:
                if cur_str not in nums:
                    self.ans = cur_str
                return

            for idx in range(2):
                dfs(cur_str + str(idx))

        dfs('')
        return self.ans

nums = ["111","011","001"]
print(S().findDifferentBinaryString(nums))

# https://leetcode.com/problems/find-unique-binary-string/discuss/1666235/Python3-DFS-backtracking-easy-understanding
