'''
https://leetcode.com/problems/find-all-groups-of-farmland/
https://leetcode.com/problems/find-all-groups-of-farmland/discuss/1444167/Python-DFS-O(MN)


'''

from typing import List
import collections

class S:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        movements = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def dfs(i, j):
            nonlocal r2, c2
            land[i][j] = 2 # visited
            for row, col in movements:
                r = i + row
                c = j + col

                if 0 <= r < len(land) and 0 <= c < len(land[0]) and land[r][c] == 1:
                    r2 = max(r2, r)
                    c2 = max(c2, c)
                    dfs(r, c)
        answer = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    r2, c2 = i, j
                    dfs(i, j)
                    answer.append((i, j, r2, c2))
        return answer

land = [[1,0,0],[0,1,1],[0,1,1]]
print(S().findFarmland(land))


