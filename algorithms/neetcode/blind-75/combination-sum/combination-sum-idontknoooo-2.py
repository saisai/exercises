'''
Approach #2. DP (Slow)
Read comment for more detail
Time Complexity: O(M*M*M*N), N = len(candidates), M = target
Space Complexity: O(M*M)

https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations
https://leetcode.com/problems/combination-sum/

'''

from typing import List

class S:

    def combinationSum(self, candiates: List[int], target: int) -> List[List[int]]:
        idx_d = {val: idx for idx, val in enumerate(candidates)} # create {num:idx}
        n = len(candidates)
        dp = [[] for _ in range(target+1)]
        for i in range(1, target+1):        # from 1 to target, O(M)
            for j in range(i):              # O(M): for all previous calculated numbers
                for comb in dp[j]:          # O(MO worst: check each of their combinations
                    start_idx = idx_d[comb[-1]] # use start_idx to avoid repetats
                    for val in candidates[start_idx:]:  # O(N): try all candidates
                        if val + j == i: dp[i].append(comb + [val])

            for candidate in candidates:    # O(N): directly from canidates not from previous result
                if candidate == i: dp[i].append([candidate])
        return dp[-1]

candidates = [2,3,6,7]
target = 7
print(S().combinationSum(candidates, target))
