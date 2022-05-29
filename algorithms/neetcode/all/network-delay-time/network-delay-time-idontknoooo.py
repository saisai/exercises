"""
Approach #1.Dijkstra
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
        visited = set()
        heap = [(0, k)]
        while heap:
            cur, node = heapq.heappop(heap)
            dp[node-1] = cur
            if node not in visited:
                visited.add(node)
                n -= 1
            for nei, w in graph[node]:
                if dp[nei-1] > cur + w:
                    dp[nei-1] = cur + w
                    if nei not in visited:
                        heapq.heappush(heap, (cur + w, nei))
            if not n: return cur
        return -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(S().networkDelayTime(times, n, k))
