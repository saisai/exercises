'''
https://leetcode.com/problems/redundant-connection/discuss/328108/DFS-(Simplest)
https://leetcode.com/problems/redundant-connection/
'''

import collections
class S:

    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(s, d):
            if s not in seen:
                seen.add(s)
                if s == d:
                    return True
                return any(dfs(n, d) for n in graph[s])
            return False

        for u, v in edges:
            seen = set()
            if dfs(u, v):
                return [u, v]

            graph[u].add(v)
            graph[v].add(u)

edges = [[1,2],[1,3],[2,3]]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(S().findRedundantConnection(edges))

