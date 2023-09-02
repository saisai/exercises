"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105


_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/insert-interval/
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Find all intervals strictly to the left and to the right of new interval.  If any intervals in between they
# overlap with newInterval.  If any overlap, update start of newInterval with start of first overlap and
# update end with end of last overlap.
# Time - O(n)
# Space - O(1)
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right = 0, len(intervals) - 1
        while left < len(intervals) and intervals[left].end < newInterval.start:
            left += 1

        while right >= 0 and intervals[right].start > newInterval.end:
            right -= 1

        if left <= right:
            newInterval.start = min(newInterval.start, intervals[left].start)
            newInterval.end = max(newInterval.end, intervals[right].end)

        return intervals[:left] + [newInterval] + intervals[right+1:]


if __name__ == '__main__':

    def answer(intervals, newInterval):

        s = Solution()
        t = []
        for obj in intervals:
            t.append(Interval(obj[0], obj[1]))
        results = s.insert(t,newInterval)
        c = []
        for r in results:
            c.append([r.start, r.end])
        return(c)

    print(answer([[1,3],[6,9]], Interval(2,5) ))
    print(answer([[1,2],[3,5],[6,7],[8,10],[12,16]], Interval(4,8) ))
    print(answer([], Interval(5,7) ))
    print(answer([[1,5]], Interval(2,3) ))
    print(answer([[1,5]], Interval(2,7) ))
    #print(answer([[1,4],[4,5]]))