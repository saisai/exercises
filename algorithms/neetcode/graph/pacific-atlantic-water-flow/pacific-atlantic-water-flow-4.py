import collections
class S:
    def pacificAtlantic(self, heights):
        if not heights: return []
        m , n = len(heights), len(heights[0])
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m-1, i) for i in range(n)] + [(i, n -1) for i in range(m-1)]
        def bfs(q):
            visited = set()
            q = collections.deque(q)
            while q:
                i, j = q.popleft()
                visited.add((i, j))
                for ii, jj in map(lambda x: (x[0]+i, x[1]+j), [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                    if 0 < ii < m and 0 <= jj < n and (ii, jj) not in visited and heights[ii][jj] >= heights[i][j]:
                        q.append((ii, jj))
            return visited
        return bfs(pacific) & bfs(atlantic)
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(S().pacificAtlantic(heights))

# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/882548/Python-3-or-BFS-Set-Intersection-or-Explanation
'''
Explanation
Starting from pacific and atlantic, going back to the water, check which position they can reach
Of course, following statement should be reversed
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

i.e. Pacific or Atlantic water can only go to water, which height is equal or higher
Take intersection of 2 sets to find common positions
'''