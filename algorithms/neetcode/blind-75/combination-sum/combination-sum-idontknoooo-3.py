'''

Approach #3. DP (Fast)
Read comment for more detail
Time Complexity: O(M*M*N), N = len(candidates), M = target
Space Complexity: O(M*M)

https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations
https://leetcode.com/problems/combination-sum/

'''

from typing import List

class S:

    def combinationSum(self, candiates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for c in candidates:            # O(N): for each candidate
            for i in range(c, target+1):        # O(M): for each possible value <= target
                if i == c: dp[i].append([c])    
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]

candidates = [2,3,6,7]
target = 7
print(S().combinationSum(candidates, target))
