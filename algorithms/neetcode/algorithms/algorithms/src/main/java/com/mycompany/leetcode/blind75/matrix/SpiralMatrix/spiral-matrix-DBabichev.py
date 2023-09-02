
class S:
    def spiralOrder(self, matrix):
        n, m = len(matrix[0]), len(matrix)
        x, y, dx, dy = 0, 0, 1, 0
        ans = []
        for _ in range(m*n):
            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y+dy][x+dx] == "*":
                dx, dy = -dy, dx

            ans.append(matrix[y][x])
            matrix[y][x] = "*"
            x, y = x + dx, y + dy
        return ans


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(S().spiralOrder(matrix))
