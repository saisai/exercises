'''
https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid
https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/discuss/1442967/python-3-dp-matrix-padding-prefix-sum-explanation

Intuition
    Brute force way is to pick all 4 nodes combinations, then:
        Check whether they are Rhombus
        Calculate its boarder sum
    This is obvious not doable given there are at most 50 * 50 = 2500 nodes
    A better way is to find sum on known Rhombus, how to get a Rhombus?
        Pick any node as bottom, expand to its left & right and find the corresponding top node
    Why not think it as the left, right, top vertex?
        You can, but it depends on the way you traverse the matrix
        When traversing from left to right, top to bottom, only consider the vertex at the bottom vertex can have the information of left, right, bottom vertices

Explanation
    Since we are trying to get sum of nodes, using prefix-sum becomes almsot obvious, espesically when the lines were drawn :) on the example
    Below is an implementation of the idea I mentioned above, see comments for more detail

NOTE: I used a (n+2) * (m+2) matrix, so that I will have zero padding on the boarder, which will be eaiser when handling edge cases.

Implementation

'''

from typing import List

class S:

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0,]] * (n+2) for _ in range(m+2)]
        ans = []
        for i in range(1, m+1):
            for j in range(1, n+1):  # [i, j] will be the bottom vertex
                ans.append(grid[i-1][j-1])
                dp[i][j] = [grid[i-1][j-1], grid[i-1][j-1]]
                dp[i][j][0] += dp[i-1][j-1][0]  # dp: major diagonal
                dp[i][j][1] += dp[i-1][j+1][1]  # dp: minor diagonal
                for win in range(1, min(m,n)):
                    x1, y1 = i-win, j-win  # left vertex
                    x2, y2 = i-win,j+win # right vertex
                    x3, y3 = i-win-win, j # top vertex
                    if not (all(1 <= x < m+1 for x in [x1, x2, x3]) and all(1 <= y < n+1 for y in [y1, y2, y3])):
                        break
                    b2l = dp[i][j][0] - dp[x1-1][y1-1][0]      # bottom node to left node (node sum), major diagonal
                    b2r = dp[i][j][1] - dp[x2-1][y2+1][1]      # bottom node to right node (node sum), minor diagonal
                    l2t = dp[x1][y1][1] - dp[x3-1][y3+1][1]    # left node to top node (node sum), minor diagonal
                    r2t = dp[x2][y2][0] - dp[x3-1][y3-1][0]    # right node to top node (node sum), major diagonal
                    vertices_sum = grid[i-1][j-1] + grid[x1-1][y1-1] + grid[x2-1][y2-1] + grid[x3-1][y3-1]
                    cur = b2l + b2r + l2t + r2t - vertices_sum # sum(edges) - sum(4 vertices)
                    ans.append(cur)
        return sorted(set(ans), reverse=True)[:3]   # unique + sort reverse + keep only first 3


grids =[ [[7,7,7]], [[1,2,3],[4,5,6],[7,8,9]] , [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]] ]

for grid in grids:
    print(S().getBiggestThree(grid))
