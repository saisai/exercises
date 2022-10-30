'''
https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/solutions/855377/python-3-dp-omn-time-in-place-explanation/

'''

from typing import List

class S:
    '''
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid[0][0] = grid[0][0], grid[0][0]                                     # (small, large) for starting point

        for j in range(1, n):
            grid[0][1] = grid[0][j-1] * grid[0][j], grid[0][j-1][1]*grid[0][j]  # special handling first row
        for i in range(1, m):
            grid[i][0] = grid[i-1][0][0]*grid[i][0], grid[i-1][0][1]*grid[i][0] # special handling first col
        for i in range(1, m):
            for j in range(1, n):
                nums = [grid[i-1][j][0]*grid[i][j], grid[i][j-1][0]*grid[i][j], grid[i-1][j][1]*grid[i][j], grid[i][j-1][1]*grid[i][j]]
                small, large = min(nums), max(nums)
                grid[i][j] = (small, large)                                     # update all other points
        return (grid[-1][-1][1] % 1000000007) if grid[-1][-1][1] >= 0 else -1
    '''
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid[0][0] = grid[0][0], grid[0][0]                                      # (small, large) for starting point
        for j in range(1, n):
            grid[0][j] = grid[0][j-1][0]*grid[0][j], grid[0][j-1][1]*grid[0][j]  # special handling first row
        for i in range(1, m):
            grid[i][0] = grid[i-1][0][0]*grid[i][0], grid[i-1][0][1]*grid[i][0]  # special handling first col
        for i in range(1, m):
            for j in range(1, n):
                nums = [grid[i-1][j][0]*grid[i][j], grid[i][j-1][0]*grid[i][j], grid[i-1][j][1]*grid[i][j], grid[i][j-1][1]*grid[i][j]]
                small, large = min(nums), max(nums)
                grid[i][j] = (small, large)                                      # update all other points
        return (grid[-1][-1][1] % 1000000007) if grid[-1][-1][1] >= 0 else -1

grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
print(S().maxProductPath(grid))

