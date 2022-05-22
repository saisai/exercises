
import collections

class S:

    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0]: return -1
        m, n = len(grid), len(grid[0])
        q = collections.deque([(0, 0, 1)])

        while q:
            x, y, step = q.popleft()
            if (x, y) == (m-1, n-1): return step
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1):
                xx, yy = x + dx, y + dy
                if 0 <=xx < m and 0 <= yy < n and not grid[xx][yy]:
                    grid[xx][yy] = 1
                    q.append((xx, yy, step + 1))
        return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]
print(S().shortestPathBinaryMatrix(grid))

# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# https://leetcode.com/submissions/detail/700531053/

