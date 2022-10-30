
'''
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/number-of-islands/solutions/863366/python-3-dfs-bfs-union-find-all-3-methods-explanation/

Approach #1. DFS
    Iterate over the matrix and DFS at each point whenever a point is land (1)
    Mark visited as 2 to avoid revisit
    Increment ans each time need to do a DFS (original, not recursive)
'''
from typing import List

class S:

    def numIslands(self, grid: List[List[str]]) -> str:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(i, j):
            grid[i][j] = '2'
            for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                ii, jj = i+di, j+dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                    dfs(ii, jj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(S().numIslands(grid))
