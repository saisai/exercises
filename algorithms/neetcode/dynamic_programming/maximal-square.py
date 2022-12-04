
from typing import List

class S:

    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # dynamic programming: bottom up
        # recursive: top down
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} # map each(r, c) -> maxLength of square

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]
        helper(0, 0)
        return max(cache.values()) ** 2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(S().maximalSquare(matrix))
