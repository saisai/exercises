'''
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/number-of-islands/solutions/863366/python-3-dfs-bfs-union-find-all-3-methods-explanation/

Approach #3. Union Find
    Create dictionary d[(i,j)] = idx, give (x,y) an id number, for eaiser union find
    Create a Union Find object with length of number of "1" (say length is n or size)
    Iterate over matrix, from left to right, from top to bottom
        Union current and left or right, if they are both 1
        For each union, decrement size
    Return size
'''

from typing import List

class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.n = n
        self.size = n

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.size -= 1
            self.p[pj] = pi

    def find(self, i):
        if i != self.p[i]:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

class S:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m , n = len(grid), len(grid[0])
        d = dict()
        idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    d[i, j] = idx
                    idx += 1
        uf = UF(idx)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(d[i-1, j], d[i, j])
                    if j > 0 and grid[i][j-1] == '1':
                        uf.union(d[i, j-1], d[i, j])
        return uf.size


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(S().numIslands(grid))