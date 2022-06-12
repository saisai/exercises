
'''
BFS

https://leetcode.com/problems/number-of-provinces/discuss/303150/python-union-find-dfs-bfs
https://leetcode.com/problems/number-of-provinces/
'''
from typing import List

class S:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        if not isConnected: return 0
        s = len(isConnected)
        seen = set()
        cnt = 0
        for i in range(s):
            if i not in seen:
                q = [i]
                while q:
                    p = q.pop(0)
                    if p not in seen:
                        seen.add(p)
                        q += [k for k, adj in enumerate(isConnected[p]) if adj and (k not in seen)]
                cnt += 1
        return cnt
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(S().findCircleNum(isConnected))
