
class Solution:

    def __call__(self, candidates, target):
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                #res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res
print(Solution()([2,3,6,7], 7))
print(Solution()([2,3,5], 8))

# https://leetcode.com/problems/combination-sum/
# https://www.youtube.com/watch?v=GBKI9VSKdGg&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=8&ab_channel=NeetCode
