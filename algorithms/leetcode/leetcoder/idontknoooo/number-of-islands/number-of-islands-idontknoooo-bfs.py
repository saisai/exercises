'''
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/number-of-islands/solutions/863366/python-3-dfs-bfs-union-find-all-3-methods-explanation/
Approach #2. BFS
    Iterate over the matrix and BFS at each point whenever a point is land (1)
    Mark visited as 2 to avoid revisit
    Increment ans each time need to do a BFS (original, not recursive)
'''
from typing import List
import collections

class S:

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: return 0
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q = collections.deque([(i, j)])
                    grid[i][j] = '2'
                    while q:
                        x, y = q.popleft()
                        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                            xx, yy = x+dx, y+dy
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                                q.append((xx, yy))
                                grid[xx][yy] = '2'
                    ans += 1
        return ans

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(S().numIslands(grid))
