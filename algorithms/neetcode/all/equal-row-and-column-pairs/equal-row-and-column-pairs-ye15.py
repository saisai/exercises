
from collections import Counter
from typing import List

class S:

    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = Counter(tuple(row) for row in grid)
        return sum(freq[tuple(col)] for col in zip(*grid))

grid = [[3,2,1],[1,7,6],[2,7,7]]
print(S().equalPairs(grid))
