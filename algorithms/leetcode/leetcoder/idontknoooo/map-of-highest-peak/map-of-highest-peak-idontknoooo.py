'''

https://leetcode.com/problems/map-of-highest-peak/discuss/1442614/python-3-greedy-multi-source-bfs-explanation

https://leetcode.com/problems/map-of-highest-peak/

Explanation
Start from water nodes and BFS until all heights are found
NOTE: You don't need to worry about getting a skewed peak (by skewed, I mean a height with difference greater than 1 on some neighbors), because it will never be possible
For example: following situation will never be possible
1 2
1 0
This is because we are using BFS and increment at 1 for each step, in this case, for any node at (i, j), whenever the value is assigned, it will be the highest possible value
If the same node is re-visited in later step, it can only be the same or larger (larger will be wrong, since you will get a skewed peak), thus, no need to revisited any assigned node (i, j)
Implementation

'''

from typing import List
import collections

class S:

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        arr =collections.deque()
        m, n = len(isWater), len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    arr.append((0, i, j))
        print(arr)

        ans = [[-1] * n for _ in range(m)]
        print(ans)

        while arr:
            val, x, y = arr.popleft()
            if ans[x][y] != -1: continue
            ans[x][y] = val
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x+dx, y+dy
                if 0 <= xx < m and 0 <= yy < n and ans[xx][yy] == -1:
                    arr.append((val+1, xx, yy))
        return ans

isWater = [[0,1],[0,0]]
print(S().highestPeak(isWater))
