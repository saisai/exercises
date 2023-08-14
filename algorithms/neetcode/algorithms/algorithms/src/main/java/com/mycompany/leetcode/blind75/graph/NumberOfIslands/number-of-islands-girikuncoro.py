

class S:

    def numIslands(self, grid):
        if not grid:
            return 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or j >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return

            grid[i][j] = '#'
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(S().numIslands(grid))
