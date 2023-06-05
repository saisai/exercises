
from typing import List
import itertools

class S:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        merged = list(itertools.chain(*grid))
        n = int(len(merged) / m)
        shift = k % len(merged)
        for i in range(shift):
            last = merged.pop()
            merged.insert(0, last)
        return [merged[i: i+n] for i in range(0, len(merged), n)]
    

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

print(S().shiftGrid(grid, k))