from typing import List

class S:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        moves = [[1, 2], [2, 1], [1, -2], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
        x, y, m = 0, 0, len(grid)
        if grid[x][y]:
            return False
        cnt = 0
        while cnt < m * m - 1: # stop when all positions are met
            for dx, dy in moves: # for eacht position, check all 8 direction adn search gredily
                xx, yy = x+dx, y+dy
                if 0 <= xx < m and 0 <= yy < m and grid[xx][yy] == cnt + 1:
                    cnt += 1
                    grid[xx][yy] = -1
                    x, y = xx, yy
                    break       # once found, break -> gready
            else:
                return False    # if none found, meaning the config is wrong
        return True

grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
print(S().checkValidGrid(grid))
