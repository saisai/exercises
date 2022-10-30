'''
https://leetcode.com/problems/check-if-matrix-is-x-matrix/discuss/2198405/python3-enumerate-elements
https://leetcode.com/problems/check-if-matrix-is-x-matrix/

'''
from typing import List

class S:

    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        n = len(grid)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if ( i == j or i+j == n - 1 ) and not x or i != j and i + j != n-1 and x: return False
        return True

grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
print(S().checkXMatrix(grid))
