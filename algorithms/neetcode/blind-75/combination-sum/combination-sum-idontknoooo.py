'''
Approach #1. DFS (Backtracking)
Straight forward backtracking
cur: current combination, cur_sum current combination sum, idx index current at (to avoid repeats)
Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
Space complexity: O(M/min_cand)

https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations
https://leetcode.com/problems/combination-sum/

'''

from typing import List

class S:

    def combinationSum(self, candiates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(cur,cur_sum, idx):          # try out each possible cases
            if cur_sum > target: return     # this is the case, cur_sum will never equal to target
            if cur_sum == target: ans.append(cur); return # if equal, add to ans
            for i in range(idx, n): dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # DFS
        dfs([], 0, 0)
        return ans

candidates = [2,3,6,7]
target = 7
print(S().combinationSum(candidates, target))
