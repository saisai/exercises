
from typing import List
from math import inf
class S:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        n = len(vals)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = -inf
        for i, u in enumerate(graph):
            u.sort(key=vals.__getitem__, reverse=True)
            cand = vals[i] + sum(max(0, vals[x]) for x in u[:k])
            ans = max(ans, cand)
        
        return ans 
    
vals = [1,2,3,4,10,-10,-20]
edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
k = 2
    
print(S().maxStarSum(vals, edges, k))