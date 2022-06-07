'''
https://leetcode.com/problems/minimum-cost-for-tickets/discuss/1199803/Python-Basic-Recursion
https://leetcode.com/problems/minimum-cost-for-tickets/

'''

import functools


from typing import List


class S:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        days = set(days)
        graph = {0: 1, 1: 7, 2: 30}

        @functools.lru_cache(None)
        def recurse(day, end):

            if day > end:
                return 0
            if day not in days:
                return recurse(day+1, end)

            return min([
                c + recurse(day+graph[i], end)
                for i, c in enumerate(costs)
                ])
        return recurse(1, max(days))

days = [1,4,6,7,8,20]
costs = [2,7,15]
print(S().mincostTickets(days, costs))

