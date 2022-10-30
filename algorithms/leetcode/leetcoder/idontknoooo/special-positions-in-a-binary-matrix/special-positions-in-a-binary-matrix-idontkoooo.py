'''
https://leetcode.com/problems/special-positions-in-a-binary-matrix/
https://leetcode.com/problems/special-positions-in-a-binary-matrix/solutions/844056/python-3-hash-tab/

'''

from typing import List

class S:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans, m, n = 0, len(mat), len(mat[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                row[i] += mat[i][j]
                col[j] += mat[i][j]
        for i in range(m):
            for j in range(n):
                if mat[i][j] and row[i] == 1 and col[j]  == 1: ans +=1; break
        return ans

mat = [[1,0,0],[0,0,1],[1,0,0]]
print(S().numSpecial(mat))
