

class S:

    def shiftGrid(self, grid, k):

        m, n = len(grid), len(grid[0])

        print(m, n)
        res = [[0] * n for _ in range(m)]

        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                pos = (i * n + j + k) % (m*n)
                newI, newJ = divmod(pos, n)
                res[newI][newJ] = num

        return res


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(S().shiftGrid(grid, k))

# https://leetcode.com/problems/shift-2d-grid/discuss/2006916/python-3-oror-simple-solution-oror-O(mn)O(mn)
