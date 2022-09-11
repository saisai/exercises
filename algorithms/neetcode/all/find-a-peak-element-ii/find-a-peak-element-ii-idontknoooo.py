'''
Explanation
    Below code is an implementation to hint section
    Start from mid column, if a peak is found in this column, return its location
        If peak is on the left, then do a binary search on the left side columns between [left, mid-1]
        If peak is on the right, then do a binary search on the right side columns between [mid+1, right]

Time: O(m*log(n))
Space: O(1)
Thanks @andy_ng for helping improve this solution

Implementation

https://leetcode.com/problems/find-a-peak-element-ii/discuss/1446385/python-3-binary-search-explanation
https://leetcode.com/problems/find-a-peak-element-ii/

'''

from typing import List

class S:

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            cur_max, left = 0, False
            for i in range(m):
                if i > 0 and mat[i-1][mid] >= mat[i][mid]:
                    continue
                if i + 1 < m and mat[i+1][mid] >= mat[i][mid]:
                    continue
                if mid + 1 < n and mat[i][mid+1] >= mat[i][mid]:
                    cur_max, left = mat[i][mid], not mat[i][mid] > cur_max
                    continue
                if mid > 0 and mat[i][mid-1] >= mat[mid][mid]:
                    cur_max, left = mat[i][mid], mat[i][mid] > cur_max
                    continue
                return [i, mid]
            if left:
                r = mid - 1
            else:
                l = mid + 1
        return []

mats = [ [[1,4],[3,2]], [[10,20,15],[21,30,14],[7,16,32]] ]

for mat in mats:
    print(S().findPeakGrid(mat))
