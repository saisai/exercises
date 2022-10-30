'''

https://leetcode.com/problems/map-of-highest-peak/discuss/1074561/Python3-bf
https://leetcode.com/problems/map-of-highest-peak/

'''

from typing import List
import collections

class S:

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0]) # dimensions
        queue = [(i,j) for i in range(m) for j in range(n) if isWater[i][j]]

        print(queue)

        ht = 0
        ans = [[0] * n for _ in range(m)]
        seen = set(queue)

        while queue:
            newq =[]
            for i, j in queue:
                ans[i][j] = ht
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen:
                        newq.append((ii, jj))
                        seen.add((ii, jj))
            queue = newq
            ht += 1
        return ans
        
        '''
        alternative solution

        m, n = len(isWater), len(isWater[0]) # dimensions

        ans = [[-1]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j))
                    ans[i][j] = 0

        while queue:
            i, j = queue.popleft()
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= ii < m and 0 <= jj < n and ans[ii][jj] == -1:
                    ans[ii][jj] = 1 + ans[i][j]
                    queue.append((ii, jj))
        return ans

        '''

isWater = [[0,1],[0,0]]
print(S().highestPeak(isWater))
