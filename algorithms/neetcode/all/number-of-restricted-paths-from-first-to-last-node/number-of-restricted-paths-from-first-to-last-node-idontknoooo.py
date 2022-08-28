'''
https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/discuss/1432248/python-3-dijkstra-dfs-dag-pruning-explanation

Implementation
    The solution is basically an implementation based on hint, please seee below comments for detail
Explanation
'''

from typing import List
import collections
import heapq
from functools import cache

class S:

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        graph = collections.defaultdict(list) # build graph
        for a, b, w in edges:
            graph[a].append((w, b))
            graph[b].append((w, a))

        print(graph)
        heap = graph[n]
        heapq.heapify(heap)
        d = {n: 0}
        while heap:     # Dijkstra from node `n` to other nodes, record shortest distance to each node
            cur_w, cur = heapq.heappop(heap)
            if cur in d: continue
            d[cur] = cur_w
            for w, nei in graph[cur]:
                heapq.heappush(heap, (w+cur_w, nei))
        graph = collections.defaultdict(list)
        for a, b, w in edges: # pruning based on `restriced` condition, make unidirected graph to directed-acyclic graph
            if d[a] > d[b]:
                graph[a].append(b)
            elif d[a] < d[b]:
                graph[b].append(a)
        ans, mod = 0, int(1e9+7)
        @cache
        def dfs(node):          # use DFS to find total number of paths
            if node == n:
                return 1
            cur = 0
            for nei in graph[node]:
                cur = ( cur + dfs(nei)) % mod
            return cur
        return dfs(1)

n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
print(S().countRestrictedPaths(n, edges))
