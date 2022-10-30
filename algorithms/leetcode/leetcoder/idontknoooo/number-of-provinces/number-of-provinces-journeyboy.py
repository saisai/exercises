
'''
union find:

https://leetcode.com/problems/number-of-provinces/discuss/303150/python-union-find-dfs-bfs
https://leetcode.com/problems/number-of-provinces/
'''
from typing import List

class UnionFind:

    def __init__(self, n):
        self.u = list(range(n))

    def union(self, a, b):
        ra, rb = self.find(a),  self.find(b)
        if ra != rb: self.u[ra] = rb

    def find(self, a):
        while self.u[a] != a: a = self.u[a]
        return a

class S:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        s = len(isConnected)

        uf = UnionFind(s)
        for r in range(s):
            for c in range(r, s):
                if isConnected[r][c] == 1:
                    uf.union(r, c)
        return len(set([uf.find(i) for i in range(s)]))
    

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(S().findCircleNum(isConnected))
