'''
https://leetcode.com/problems/find-right-interval/
https://leetcode.com/problems/find-right-interval/solutions/815413/python-3-binary-search-explanation/

Intuition
    We could brutal force it which takes O(n*n), or we can also sort + binary search which will take O(nlgn)

Explanation
    Since we need to sort the interval list, we want to store the original index for final results
        intervals = [interval + [i] for i, interval in enumerate(intervals)]
    For each interval, we do a binary search begin with i+1 and end with n-1
        If condition r <= intervals[mid][0] holds, we push the right margin to left by doing end = mid - 1 because we want the possible value close to the left side as possible.
        If condition doesn't hold, we do the opposite to look for a possible interval
    Once we find the most left index (closest interval), use original index of current interval (ori_idx) and apply the closest right interval's original index (intervals[begin][2]) to it.
    Return ans
'''

from typing import List

class S:

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        intervals = [interval + [i] for i, interval in enumerate(intervals)]

        intervals.sort()
        n = len(intervals)
        ans = [-1] * n
        for i, vals in enumerate(intervals):
            (_, r, ori_idx) = vals
            begin, end = i + 1, n - 1
            while begin <= end:
                mid = (begin + end) // 2
                if r <= intervals[mid][0]: end = mid - 1
                else: begin = mid + 1
            ans[ori_idx] = intervals[begin][2] if begin < n else -1
        return ans

intervals = [[3,4],[2,3],[1,2]]
print(S().findRightInterval(intervals))

