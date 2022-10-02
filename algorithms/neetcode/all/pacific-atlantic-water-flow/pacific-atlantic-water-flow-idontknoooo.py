'''

https://leetcode.com/problems/pacific-atlantic-water-flow/
https://leetcode.com/problems/pacific-atlantic-water-flow/solutions/882548/python-3-bfs-set-intersection-explanation/

Explanation
Starting from pacific and atlantic, going back to the water, check which position they can reach
    Of course, following statement should be reversed
        Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

    i.e. Pacific or Atlantic water can only go to water, which height is equal or higher
Take intersection of 2 sets to find common positions
'''
import collections

from typing import List

class S:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m-1)]
        def bfs(q):
            visited = set()
            q = collections.deque(q)
            while q:
                i, j = q.popleft()
                visited.add((i, j))
                for ii, jj in map(lambda x: (x[0]+i, x[1]+j), [(-1,0), (1, 0), (0, -1), (0,1)]):
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited and matrix[ii][jj] >= matrix[i][j]:
                        q.append((ii, jj))
            return visited
        
        test_pacific = bfs(pacific)
        test_atlantic = bfs(atlantic)
        print(test_pacific)
        print(test_atlantic)

        return bfs(pacific) & bfs(atlantic)

matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
result = S().pacificAtlantic(matrix)

print(sorted(result))


