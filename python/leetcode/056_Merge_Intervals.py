"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-intervals/
# Given a collection of intervals, merge all overlapping intervals.

# Sort intervals by start points.  If interval starts before previous interval ends then merge, else add to result.
# Time - O(n log n)
# Space - O(1)
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[%s, %s]' %(self.start, self.end)

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        intervals.sort(key=lambda x: x.start)
        merged = []

        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged

if __name__ == '__main__':

    def answer(intervals):

        s = Solution()
        t = []
        for obj in intervals:
            t.append(Interval(obj[0], obj[1]))
        results = s.merge(t)
        c = []
        for r in results:
            c.append([r.start, r.end])
        return(c)

    print(answer(intervals = [[1,3],[2,6],[8,10],[15,18]]))
    print(answer(intervals = [[1,4],[4,5]]))

