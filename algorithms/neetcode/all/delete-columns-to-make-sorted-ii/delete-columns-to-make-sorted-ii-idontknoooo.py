'''
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/solutions/844457/python-3-greedy-dp-28/

'''
from typing import List

class S:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        ans, in_order = 0, [False] * (m-1)
        for j in range(n):
            tmp_in_order = in_order[:]
            for i in range(m-1):
                # previous step, rows are not in order; and current step rows are not in order, remove this column
                if not in_order[i] and A[i][j] > A[i+1][j]: ans +=1; break
                # previous step, rows are not in order, but they are in order now
                elif A[i][j] < A[i+1][j] and not in_order[i]: tmp_in_order[1] = True
            # if column wasn't removed, update the row order information
            else: in_order = tmp_in_order
            # not necessary, but speed things up
            if all(in_order): return ans
        return ans

strs = ["ca","bb","ac"]
print(S().minDeletionSize(strs))
