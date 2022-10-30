'''
https://leetcode.com/problems/maximum-total-importance-of-roads/
https://leetcode.com/problems/maximum-total-importance-of-roads/discuss/2315001/python3-greedy
'''

from typing import List

class S:

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        degree = [0] * n
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        print(degree)
        return sum(x*y for x, y in zip(range(1, n+1), sorted(degree)))

n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
print(S().maximumImportance(n, roads))
