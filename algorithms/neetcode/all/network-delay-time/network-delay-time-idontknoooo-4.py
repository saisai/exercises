"""
Approach #4.SPFA(deque implementation)
https://leetcode.com/problems/network-delay-time/discuss/1614297/python-3-different-4-methods-no-explanation
"""

import sys

import heapq
import collections
class S:

    def networkDelayTime(self, times, n, k):

        dp = [sys.maxsize] * n
        dp[k-1] = 0
        graph = collections.defaultdict(list)
        for s, e, w in times:
            graph[s].append((e, w))

        dq = collections.deque([k])
        visited = set([k])
        while dq:
            node = dq.popleft()
            cost = dp[node-1]
            visited.remove(node)
            for nei, w in graph[node]:
                if dp[nei-1] > cost + w:
                    dp[nei-1] = cost + w
                    if nei not in visited:
                        visited.add(nei)
                        dq.append(nei)

        ans = 0
        for i in range(n):
            if i != k-1:
                ans = max(ans, dp[i])
        return ans if ans != sys.maxsize else -1



times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(S().networkDelayTime(times, n, k))
