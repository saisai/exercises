
class S:
    def pacificAtlantic(self, heights):
        def dfs(r, c, h, o):
            if r < 0 or c < 0 or r == m or c == n:
                return

            if values[r][c] & o:
                return

            if heights[r][c] < h:
                return

            values[r][c] |= o
            if values[r][c] == 3:
                result.append([r, c])

            h = heights[r][c]
            dfs(r-1, c, h, o)
            dfs(r+ 1, c, h,o)
            dfs(r, c - 1, h, o)
            dfs(r, c + 1, h, o)

        m = len(heights)
        n = len(heights[0])
        result = []
        values = [[0] * n for _ in range(m)]

        for c in range(n):
            dfs(0, c, 0, 1)
            dfs(m-1, c, 0, 2)

        for r in range(m):
            dfs(r, 0, 0, 1)
            dfs(r, n-1, 0, 2)

        return result
        

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(S().pacificAtlantic(heights))

# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/1755572/Python-DFS
