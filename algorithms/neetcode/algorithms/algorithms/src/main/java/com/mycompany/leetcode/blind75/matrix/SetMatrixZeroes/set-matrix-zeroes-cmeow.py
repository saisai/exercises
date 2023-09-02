from typing import List

class S:
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        zeroes_row = [False] * m
        zeroes_col = [False] * n
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True 
                    
        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
        return matrix
                    
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(S().setZeroes(matrix))