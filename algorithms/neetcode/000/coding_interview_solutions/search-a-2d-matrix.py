
class S:

    def searchMatrix(self, matrix, target):

        ROWS, COLS = len(matrix), len(matri[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot ) // 2
            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not ( top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:

