'''
https://www.youtube.com/watch?v=FXWRE67PLL0&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=13&ab_channel=NeetCode

https://leetcode.com/problems/redundant-connection/
'''
class S:

    def findRedundantConnection(self, edges):
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if cant complete
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
edges = [[1,2],[1,3],[2,3]]
print(S().findRedundantConnection(edges))

