'''
The second approach is DFS. Since the DFS searches the graph down to the end (the node with no outbound edges) and those nodes should be put at the end of the order, we can use this feature to build the topological order in reserved order: each time we reach the end of a DFS or finish searching the node (so it has no unvisited outbound edges), we put it at the back of the remaining sequence.

In such way, we only need to build one destination graph, setting edges as source->destination. There is no need to remove any edges. And once we detect any directed cycle in DFS, we can stop right away. So I think DFS is a better way to do topological sort. And each time we finised search a branch, the root of branch has no unvisitied outbound edges and we can safely add it into the order.

And cycle can be detected during the DFS. And we need to set 3 visit status. 0 -> not visited; 1 -> visited, -1 -> visited and in the same DFS branch. So if we meet a node with status -1, we find a directed cycle. If we meet a node with status 1, we stop DFS from that node.


https://leetcode.com/problems/course-schedule-ii/discuss/266867/Python-Topological-Sort-BFS-and-DFS-(reserve-order)
https://leetcode.com/problems/course-schedule-ii/
'''
from typing import List

class S:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        G = [set() for _ in range(numCourses)]
        for d, s in prerequisites:
            G[s].add(d)
        vis, orders = [0] * numCourses, []

        def dfs_circle(x):
            vis[x] = -1
            for y in G[x]:
                if vis[y] < 0 or (not vis[y] and dfs_circle(y)):
                    return True
            vis[x] = 1
            orders.append(x)
            return False
        for x in range(numCourses):
            if not vis[x] and dfs_circle(x):
                return []
        return orders[::-1]
    

numCourses = 2
prerequisites = [[1,0]]

print(S().findOrder(numCourses, prerequisites))

