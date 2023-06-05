
from collections import deque
from typing  import List

class S:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        if not grid:
            return -1
        M, N = len(grid), len(grid[0])
        if M == 1 and N == 1:
            return 0
        if k > M+N-2:
            return M + N - 2
        
        target = (M-1, N-1)
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pool = deque()
        pool.append((0,0, k))
        visited = {(0, 0): k}
        cnt = 0
        
        while pool:
            tp = deque()
            while pool:
                x, y, p = pool.popleft()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if(nx, ny) == target:
                            return cnt + 1
                        np = p - grid[nx][ny]
                        if np < 0:
                            continue
                        if(nx, ny) in visited:
                            if np > visited[(nx, ny)]:
                                tp.append((nx, ny, np))
                                visited[(nx, ny)] = np
                        else:
                            tp.append((nx, ny, np))
                            visited[(nx, ny)] = np
            pool = tp
            cnt += 1
        return -1

grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
print(S().shortestPath(grid, k))
                            
        