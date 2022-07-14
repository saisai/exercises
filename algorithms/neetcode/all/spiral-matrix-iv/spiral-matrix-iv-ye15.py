''
https://leetcode.com/problems/spiral-matrix-iv/
https://leetcode.com/problems/spiral-matrix-iv/discuss/2239171/python3-rotation
'''

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class S:

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        ans = [[-1] * n for _ in range(m)]
        node = head
        i, j, di, dj = 0, 0, 0, 1
        while node:
            ans[i][j] = node.val
            node = node.next
            if not (0 <= i + di < m and 0 <= j+dj < n and ans[i+di][j+dj] == -1):
                di, dj = dj, -di
            i, jd = i+di, j+dj
        return ans


m = 3
n = 5
head = [3,0,2,6,8,1,7,9,4,2,5,5,0]

print(S().spiralMatrix(m, n, head))

