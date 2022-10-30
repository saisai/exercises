'''
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/discuss/1477844/python-3-bitmask-clean-omn-explanation

Explanation
    It's not a difficult question and yes, some us might be overthinking it.
    If 1 columns is flipped, then each row in this column will be fliped.
    Thus, the result is pre-determined, we can find the answer without flipping any columns.
    How to decide? Count the bitmask for each row or the opposite of its bitmask
    Below two rows' bitmask are opposite to each other, thus they will be considered at the same one
        001
        110
    For simplicity, let's make sure bitmask always start with 0.
        If the first number of current row is 0, it's natually start from 0
        If the first number of current row is 1, we will take the opposite bit for each element in this row (i.e. 1 -> 0, 0 -> 1)
    Return the maximum of frequency

Implementation
    Simplified version

'''
import collections
from typing import List

class S:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = collections.defaultdict(int)                # hashmap for counting
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            reverse = not matrix[i][0]                  # decide whether need to reverse bit
            cur = ''.join(['0' if matrix[i][j] ^ reverse else '1' for j in range(n)]) # see below solution for expaned code
            d[cur] += 1         # count frequency
        return max(d.values())

matrix = [[0,1],[1,0]]
print(S().maxEqualRowsAfterFlips(matrix))


