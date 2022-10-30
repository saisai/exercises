'''
https://leetcode.com/problems/bricks-falling-when-hit/
https://leetcode.com/problems/bricks-falling-when-hit/solutions/950348/python-3-dfs-explanation/

'''
from typing import List

class S:

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(x, y):
            if grid[x][y] != 1: return 0
            grid[x][y], ans = 2, 1
            for xx, yy in map(lambda pair: (pair[0]+x, pair[1]+y), ((-1, 0), (1, 0), (0, -1), (0, 1))):
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1:
                    ans += dfs(xx, yy)
            return ans

        def is_stable(x, y):
            grid[x][y] += 1
            if grid[x][y] <= 0: return False
            if (x == 0 and grid[x][y] == 1) or grid[x][y] == 2: return True
            return any((0 <= xx < m and 0 <= yy < n) and grid[xx][yy] == 2 for xx, yy in map(lambda pair: (pair[0]+x, pair[1]+y), ((-1, 0), (1, 0), (0, -1), (0, 1))))

        m, n = len(grid), len(grid[0])
        for x, y in hits: grid[x][y] -= 1
        for j in range(n): dfs(0, j)
        return [(dfs(x, y) - 1) if is_stable(x, y) else 0 for x, y in hits[::-1]][::-1]


grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
print(S().hitBricks(grid, hits))
