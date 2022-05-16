class S:
    def uniquePath(self, nums):
        res = []
        perm = []
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()
        dfs()
        return res

nums = [1, 2, 1]
print(S().uniquePath(nums))
# https://leetcode.com/problems/permutations-ii/discuss/1935052/Python-or-Faster-than-92.91-or-Backtracking
# https://leetcode.com/problems/permutations-ii/discuss/1910839/Python-backtracking-solution-time-92.77-space-54.17
