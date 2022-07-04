'''
Explanation
Simulate the process
When current board is 1 (right), ball will move to right only if the right neighbor of current position is also 1
When current board is -1 (left), ball will move to left only if the left neighbor of current position is also -1
Repeat above process until the ball drop to bottom or return -1 if it won't
DFS is not necessary, you can implement it using an iterative way instead
Time: O(m*n)
Implementation

https://leetcode.com/problems/where-will-the-ball-fall/discuss/1443268/python-3-dfs-simulation-explanation
https://leetcode.com/problems/where-will-the-ball-fall/

'''
from typing import List
from functools import cache

class S:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        @cache
        def helper(r, c):
            if r == m:
                return c
            elif grid[r][c] == 1 and c+1 < n and grid[r][c+1] == 1:
                return helper(r+1, c +1)
            elif grid[r][c] == -1 and 0 <= c - 1 and grid[r][c-1] == -1:
                return helper(r+1, c-1)
            else:
                return -1

        return [helper(0, j ) for j in range(n)]
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]

print(S().findBall(grid))

