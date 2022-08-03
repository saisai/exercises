'''

https://leetcode.com/problems/spiral-matrix/discuss/1948758/python-3-in-place-greedy-explanation
https://leetcode.com/problems/spiral-matrix/

Explanation
Idea: move to one direction until you can't. Mark visited node as -101 (out of range by description)
move = [right, down, left, up] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
i: pointer for move, use mod 4 to make sure i in [0, 3]
Time: O(m*n)
Implementation
'''

from typing import List

class S:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(matrix), len(matrix[0])
        i, x, y = 0, 0, -1
        ans = []
        for _ in range(m*n):
            while not (0 <= x+move[i][0] < m and 0 <= y+move[i][1] < n and matrix[x+move[i][0]][y+move[i][1]] >= -100):
                i = ( i + 1) % 4
            x, y = x+move[i][0], y+move[i][1]
            ans.append(matrix[x][y])
            matrix[x][y] = -101
        return ans

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(S().spiralOrder(matrix))
