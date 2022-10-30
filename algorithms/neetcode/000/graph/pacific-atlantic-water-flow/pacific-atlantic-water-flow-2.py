
from collections import deque

class S:
    def pacificAtlantic(self, heights):
        def bfs(q, ocean):
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    if mask[nr][nc] & ocean:
                        continue
                    mask[nr][nc] |= ocean
                    if mask[nr][nc] == 3:
                        result.append([nr, nc])
                    q.append((nr, nc))
        result = []
        m, n = len(heights), len(heights[0])
        mask = [[0] * n for _ in range(m)]
        pacific = deque()
        atlantic = deque()
        for r in range(m):
            pacific.append((r, 0))
            mask[r][0] |= 1
            atlantic.append((r, n - 1))
            mask[r][n-1] |= 2
            if mask[r][n-1] == 3:
                result.append([r, n- 1])
        for c in range(1, n):
            pacific.append((0, c))
            mask[0][c] |= 1
            if mask[0][c] == 3:
                result.append([0, c])
            atlantic.append((m - 1, n - 1 -c))
            mask[m - 1] [n - 1 - c] |= 2
            if mask[m-1][n-1-c] == 3:
                result.append([m-1, n - 1 - c])
        bfs(pacific, ocean=1)
        bfs(atlantic, ocean=2)
        return result
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(S().pacificAtlantic(heights))

# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/1773672/Python-BFS-using-bitmask