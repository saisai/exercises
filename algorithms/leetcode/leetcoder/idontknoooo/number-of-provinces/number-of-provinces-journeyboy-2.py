
'''
DFS
https://leetcode.com/problems/number-of-provinces/discuss/303150/python-union-find-dfs-bfs
https://leetcode.com/problems/number-of-provinces/
'''
from typing import List

class S:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        s = len(isConnected)
        seen = set()

        def dfs(p):
            for q, adj in enumerate(isConnected[p]):
                if (adj == 1) and (q not in seen):
                    seen.add(q)
                    dfs(p)

        cnt = 0
        for i in range(s):
            if i not in seen:
                dfs(i)
                cnt += 1
        return cnt
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(S().findCircleNum(isConnected))
