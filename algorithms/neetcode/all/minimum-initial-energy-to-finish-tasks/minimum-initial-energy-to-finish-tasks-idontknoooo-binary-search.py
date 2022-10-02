'''
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/discuss/944714/python-3-sort-greedy-sort-binary-search-explanation

Approach #1 - Binary Search
Sort by difference
Use binary search validate if given input (energy) can finish all works
Search the smallest possible (like bisect_left)

'''

from typing import List

class S:

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        print(tasks)
        tasks.sort(key=lambda x: x[0]-x[1])
        print(tasks)

        def ok(mid):
            for actual, minimum in tasks:
                if minimum > mid or actual > mid: return False
                if minimum <= mid: mid -= actual
            return True

        l, r = 0, 10 ** 9
        while l <= r:
            mid = (l + r) // 2
            if ok(mid): r = mid - 1
            else: l = mid + 1
        return l

for tasks in [ [[1,2],[2,4],[4,8]], 
            [[1,3],[2,4],[10,11],[10,12],[8,9]],
            [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
            ]:

    print(S().minimumEffort(tasks))

