"""
# https://leetcode.com/problems/n-queens/
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.

# For each column, place a queen in each possible row that does not conflict with an existing queen.
# Time - O(n^2 * n!), n possible rows for first col, n-1 for second ... etc.  each result size n^2
# Space - O(n^2 * n!)


The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9

"""


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype List[List[str]]
        """
        partials = [[]]         # solutions up to current now
        for col in range(n):
            new_partials = []
            for partial in partials:
                for row in range(n):
                    if not self.conflict(partial, row):
                        new_partials.append(partial + [row])
            partials = new_partials

        results = []
        for parital in partials:            # convert result to strings
            result = [['.'] * n for _ in range(n)]
            for col, row in enumerate(partial):
                result[row][col] = 'Q'
            for row in range(n):
                result[row] = ''.join(result[row])
            results.append(result)


        return results

    def conflict(self, partial, new_row):
        for col, row in enumerate(partial):
            if new_row == row:          # same row
                return True
            col_diff = len(partial) - col
            if abs(new_row - row) == col_diff:   # same diagnoal
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(1))
    print(s.solveNQueens(4))



