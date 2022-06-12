import pdb
from typing import List

class Solution:
    def combine(self, nn: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comb):
            #pdb.set_trace()
            if len(comb) == k:
                res.append(comb[:])
                #res.append(comb.copy())

            for ii in range(start, nn + 1):
                comb.append(ii)
                backtrack(ii + 1, comb)
                comb.pop()
        backtrack(1, [])
        return res
print(Solution().combine(4, 2))

# https://leetcode.com/problems/combinations/
# https://www.youtube.com/watch?v=q0s6m7AiM7o&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=13&ab_channel=NeetCode


