
class S:

    def shiftGrid(self, grid, k):

        M, N = len(grid), len(grid[0])

        def posToVal(r, c):
            return r * N + c

        def valToPos(v):
            return [v // N, v % N] # r, c

        res =[[0] * N for i in range(M)]
        print(res)
        for r in range(M):
            for c in range(N):
                newVal = (posToVal(r, c) + k ) % (M * N)
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]

        return res


grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(S().shiftGrid(grid, k))


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(S().shiftGrid(grid, k))

