'''
https://leetcode.com/problems/find-all-groups-of-farmland/
https://leetcode.com/problems/find-all-groups-of-farmland/discuss/1444966/python-3-bfs-deque-omn-explanation

Explanation
    Whenever a farmland 1 is met, starting a BFS until reach to the right bottom corner
    Mark visited node as -1 to avoid revisiting
    Time Complexity: O(M*N), since each node will be visited at most twice
    Space Complexity: O(M*N) for BFS deque

Implementation

'''

from typing import List
import collections

class S:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        ans = []

        for i in range(m):
            for j in range(n):
                if land[i][j] < 1: continue
                q = collections.deque([[i, j]])
                while q:
                    x, y = q.popleft()
                    if land[x][y] == -1: continue
                    land[x][y] = -1
                    for dx, dy in [[0, 1], [1, 0]]:
                        xx, yy = x + dx, y + dy
                        if xx < m and yy < n and land[xx][yy] == 1:
                            q.append([xx, yy])
                ans.append([i, j, x, y])
        return ans

land = [[1,0,0],[0,1,1],[0,1,1]]
print(S().findFarmland(land))


