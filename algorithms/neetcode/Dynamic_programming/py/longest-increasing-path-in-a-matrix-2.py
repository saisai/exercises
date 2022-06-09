from functools import cache

class S:

    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])

        #@cache
        def dfs(i, j):
            res = 1
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                res = max(res, 1 + dfs(i-1, j))
            if i + 1 < m and matrix[i+1][j] > matrix[i][j]:
                res = max(res, 1 + dfs(i + 1, j))
            if j - 1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                res = max(res, 1 + dfs(i, j - 1))
            if j + 1 < n and matrix[i][j+1] > matrix[i][j]:
                res = max(res, 1 + dfs(i, j + 1))
            return res

        return max(dfs(i, j) for i in range(m) for j in range(n))

matrix = [[9,9,4],[6,6,8],[2,1,1]]

print(S().longestIncreasingPath(matrix))

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/1513593/Python-DFS-with-Memoization
