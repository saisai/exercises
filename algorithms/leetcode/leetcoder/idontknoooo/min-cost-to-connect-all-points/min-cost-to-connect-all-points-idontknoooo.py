'''

https://leetcode.com/problems/min-cost-to-connect-all-points/
https://leetcode.com/problems/min-cost-to-connect-all-points/solutions/843995/python-3-min-spanning-t/

Explanation
    This is a typical minimum spanning tree question, it can be solved using either Kruskal or Prim's algorithm
    Below is a Prim's algorithm implementation
    Here is a wiki for Pirm's algorithm https://en.wikipedia.org/wiki/Prim%27s_algorithm
    Time Complexity: Prim's Algorithm takes O(NlgN) but the whole solution is dominated by O(N*N) due to graph creation (nested loop)
Implementation

'''
import heapq
from typing import List
import collections

class S:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
      
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)         
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break

        return ans

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(S().minCostConnectPoints(points))
