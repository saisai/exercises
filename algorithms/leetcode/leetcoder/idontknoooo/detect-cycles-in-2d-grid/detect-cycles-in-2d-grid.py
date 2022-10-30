'''

https://leetcode.com/problems/detect-cycles-in-2d-grid/
https://leetcode.com/problems/detect-cycles-in-2d-grid/solutions/806241/python-3-union-find-explanation-clean/

Intuition
    How to define a cycle in this matrix?
        There is at least ONE point (x, y), such that has at least 2 different neighbors (left, right, up, down) with same parent.
    How to implement the cycle detection?
        Use union find, we traverse the matrix from left to right, from top to bottom.
        At each point (x, y), we check its up and left neighbors, which are 2 different paths.
        A cycle will happen if (x, y) is connected with both left & up neighbors.
Use tuple to implement union find parent dictionary self.p.
Implementation

'''
from typing import List

class UF:
    def __init__(self, m, n):
        self.p = {(i, j): (i, j) for i in range(m) for j in range(n)}

    def union(self, ti, tj):
        pi, pj = self.find(*ti), self.find(*tj)
        if pi != pj:
            self.p[pj] = pi
            return False
        return True

    def find(self, i, j):
        if (i, j) != self.p[i, j]:
            self.p[i, j] = self.find(*self.p[i, j])
        return self.p[i,j]

class S:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UF(m, n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i-1][j]:
                    uf.union((i-1, j), (i, j))
                if j > 0 and grid[i][j] == grid[i][j-1]:
                    if uf.union((i, j-1), (i, j)): return True
        return False

for grid in [ [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]],
            [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]],
            [["a","b","b"],["b","z","b"],["b","b","a"]]
            ]:
    print(S().containsCycle(grid))
