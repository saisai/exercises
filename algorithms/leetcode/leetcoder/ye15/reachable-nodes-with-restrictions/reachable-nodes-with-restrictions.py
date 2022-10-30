
"""
https://leetcode.com/problems/reachable-nodes-with-restrictions/
https://leetcode.com/problems/reachable-nodes-with-restrictions/solutions/2390664/python3-dfs/
"""
from typing import List

class S:

    def reachableNodes(self, n: int, edges: List[List[int]], restrcited: List[int]) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)        
        ans = 0
        seen = set(restricted)        
        stack = [0]        
        while stack:            
            u = stack.pop()
            ans += 1
            seen.add(u)            
            #print("u ", u)
            for v in graph[u]:  
                #print("v", v, graph[u])              
                if v not in seen: stack.append(v)
        print("seen ", seen)
        return ans

n = 7
edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]

print(S().reachableNodes(n, edges, restricted))
