"""
Approach #1.Floyd-Warshall
https://leetcode.com/problems/network-delay-time/discuss/1614297/python-3-different-4-methods-no-explanation
"""

import sys

import heapq
import collections
class S:

    def networkDelayTime(self, times, n, k):

        dp = [[sys.maxsize] * n for _ in range(n)]
        graph = collections.defaultdict(list)
        for s, e, w in times:
            graph[s].append((e, w))
            dp[s-1][e-1] = w

        for i in range(n):
            dp[i][i] = 0

        for kk in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][kk] != sys.maxsize and dp[kk][j] != sys.maxsize:
                        dp[i][j] = min(dp[i][j], dp[i][kk] + dp[kk][j])
        ans = 0
        for j in range(n):
            ans = max(ans, dp[k-1][j])
        return ans if ans != sys.maxsize else -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(S().networkDelayTime(times, n, k))
