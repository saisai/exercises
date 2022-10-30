'''

https://leetcode.com/problems/shortest-bridge/
https://leetcode.com/problems/shortest-bridge/solutions/788854/python-3-manhattan-distance-9596-passed-time-limit-exceeded/

'''
import sys

from typing import List

class S:

    def shortestBridge(self, A: List[List[int]]) -> int:
        visited, groups = set(), []
        m, n = len(A), len(A[0])
        # dfs to find island
        def dfs(x, y, cur):
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                xx, yy = x+dx, y+dy
                if 0 <= xx < m and 0 <= yy < n and A[xx][yy] == 1 and (xx, yy) not in visited:
                    visited.add((xx, yy))
                    cur.append((xx, yy))
                    dfs(xx, yy, cur)

        # add 2 islands into groups
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and A[i][j] == 1:
                    cur = [(i, j)]
                    dfs(i, j, cur)
                    groups.append(cur)

        # find shortest manhattan distance
        manhattan = sys.maxsize
        for a, b in groups[0]:
            for x, y in groups[1]:
                manhattan = min(manhattan, abs(x-a) + abs(y-b))
        return manhattan - 1


for grid in [ [[0,1],[1,0]],
            [[0,1,0],[0,0,0],[0,0,1]],
            [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
            ]:
    print(S().shortestBridge(grid))

