'''

https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/discuss/1846788/python3-bfs\

'''
from typing import List
from collections import deque
from math import inf
class S:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        graph = [[] for _ in range(n)]
        trans = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            trans[v].append((u, w))

        def bfs(x, graph):
            dist = [inf] * n
            dist[x] = 0
            queue = deque([(x, 0)])
            while queue:
                u, w = queue.popleft()
                if dist[u] == w:
                    for v, ww in graph[u]:
                        if w+ww < dist[v]:
                            dist[v] = w+ww
                            queue.append((v, w+ww))
            return dist

        ds1 = bfs(src1, graph)
        ds2 = bfs(src2, graph)
        dd = bfs(dest, trans)

        ans = min(x+y+z for x, y, z in zip(ds1, ds2, dd))
        return ans if ans < inf else -1

n = 6
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5

print(S().minimumWeight(n, edges, src1, src2, dest))

