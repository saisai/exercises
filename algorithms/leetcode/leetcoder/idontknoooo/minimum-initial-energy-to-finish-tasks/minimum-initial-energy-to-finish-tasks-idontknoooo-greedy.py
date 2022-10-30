'''
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/discuss/944714/python-3-sort-greedy-sort-binary-search-explanation

Approach #2 - Greedy
Sort by difference
cur: actual cost, ans adjust by minimum so that it can start for all works

'''

from typing import List

class S:

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        print(tasks)
        tasks.sort(key=lambda x: x[0]-x[1])
        print(tasks)
        ans = cur = 0
        for cost, minimum in tasks:
            ans = min(cur-minimum, ans)
            cur -= cost
        return -ans

for tasks in [ [[1,2],[2,4],[4,8]], 
            [[1,3],[2,4],[10,11],[10,12],[8,9]],
            [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
            ]:

    print(S().minimumEffort(tasks))

