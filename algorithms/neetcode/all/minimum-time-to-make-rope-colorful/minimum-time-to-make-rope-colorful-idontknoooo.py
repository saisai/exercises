'''
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/solutions/845209/python-3-greedy-cle/
'''

from typing import List

class S:

    def minCost(self, s: str, cost: List[int]) -> int:
        n, ans = len(s), 0
        cur_sum = cur_max = cost[0]
        for i in range(1, n):
            if s[i-1] == s[i]: cur_sum, cur_max = cur_sum + cost[i], max(cur_max, cost[i])
            else: ans, cur_sum, cur_max = ans + cur_sum - cur_max, cost[i], cost[i]
        return ans + cur_sum - cur_max

colors = "abaac"
neededTime = [1,2,3,4,5]
print(S().minCost(colors, neededTime))
