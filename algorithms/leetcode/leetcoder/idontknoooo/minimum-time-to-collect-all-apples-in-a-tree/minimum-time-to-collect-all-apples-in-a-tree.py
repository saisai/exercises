'''
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solutions/624036/python-3-union-find-with-explanation/

'''

from typing import List

class UF:

    def __init__(self, n):
        self.p = [i for i in range(n)]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(2)
        if p1 != p2:
            self.p[p2] = p1

    def find(self, node):
        if self.p[node] != node:
            self.p[node] = self.find(self.p[node])
        return self.p[node]

    def count(self):
        ans = 0
        for i in self.p:
            if not i: ans += 1
        return (ans -1) * 2


class S:

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        uf = UF(n)
        for i, has in enumerate(hasApple):
            if has:
                uf.union(0, i)

        for i, (start, end) in enumerate(sorted(edges, key=lambda x: -x[0])):
            if uf.find(end) == 0:
                uf.union(0, start)
        return uf.count()

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]

print(S().minTime(n, edges, hasApple))

