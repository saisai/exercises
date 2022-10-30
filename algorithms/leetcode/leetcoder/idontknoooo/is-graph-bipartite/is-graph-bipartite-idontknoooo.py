'''
Explanation
Start from some node, marked it as 0, and make sure its neighbor it's colored as 1
Keep doing BFS or DFS on it, until you find a conflict
If no conflict then it's good
Since the nodes is not fully connected, we need to check for each node that's not being marked, hence use a for loop interating from index 0 to len(graph)
As long as each sub-graph is Bipartite, we can return True for graph that has all nodes
DFS will be faster than BFS, since BFS will incur many uncessary re-visits

https://leetcode.com/problems/is-graph-bipartite/discuss/1999283/python-3-dfs-bfs-explanation
https://leetcode.com/problems/is-graph-bipartite/
'''
import collections

class S:
    def isBipartite(self, graph):
        n = len(graph)
        graph = [set(g) for g in graph]
        colors = [-1] * n
        print(graph)
        print(colors)
        def bfs(i):
            q = collections.deque([[i, 0]])
            while q:
                idx, color = q.popleft()
                colors[idx] = color
                for nei in graph[idx]:
                    if colors[nei] >= 0:
                        if 1-color != colors[nei]:
                            return False
                        continue
                    q.append((nei, 1-color))
            return True
        for i in range(n):
            if colors[i] < 0 and not bfs(i):
                return False
        return True

graph = [[1,3],[0,2],[1,3],[0,2]]
print(S().isBipartite(graph))
