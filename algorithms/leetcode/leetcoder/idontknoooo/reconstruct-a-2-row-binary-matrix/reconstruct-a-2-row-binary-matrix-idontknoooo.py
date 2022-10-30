'''

https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/solutions/845641/python-3-greedy-expl/

Explanation
    Ultimately, we have to fill out 2 row and use exactly upper+lower values, so simply take the greedy apporach
        if upper + lower != sum(colsum), return []
        when colsum[i] == 2 and upper and lower are available, place both row and decrement variables
        when colsum[i] == 1 take whoever is larger and place 1 on cooresponding row
        when colsum[i] == 0 ignore and continue
        else return []
    u: first row
    d: second row

Implementation
'''
from typing import List

class S:

    def reconstructMatrix(self, upper: int, lower: int, column: List[int]) -> List[List[int]]:
        s, n = sum(column), len(column)
        if upper + lower != s: return []
        u, d = [0] * n, [0] * n
        for i in range(n):
            if column[i] == 2 and upper > 0 and lower > 0:
                u[i] = d[i] = 1
                upper, lower = upper -1, lower -1
            elif column[i] == 1:
                if upper > 0 and upper >= lower:
                    u[i], upper = 1, upper - 1
                elif lower > 0 and lower > upper:
                    d[i], lower = 1, lower - 1
                else: return []
            elif not column[i]: continue
            else: return []
        return [u, d]

upper = 2
lower = 1
colsum = [1,1,1]
print(S().reconstructMatrix(upper, lower, colsum))
