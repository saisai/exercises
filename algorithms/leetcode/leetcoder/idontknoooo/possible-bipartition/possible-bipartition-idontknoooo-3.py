import collections

class S:
    def possibleBipartition(self, N, dislikes):
        self.graph = collections.defaultdict(list)
        group_mapping = {}
        for (u, v) in dislikes: # Create graph
            self.graph[u].append(v)
            self.graph[v].append(u)

        visited = set()
        for i in range(1, N + 1):       # Iterate each node
            if i in visited: continue   # No need to revisit, since it's a non-directed graph
            stack = [(i, 0)]            # Use stack for BFS
            while stack:                # You can also use a deque instead of 2 while loop on stack
                tmp_stack = []
                while stack:            # ehaust current stack before go to next layer (BFS)
                    cur_node, group = stack.pop()
                    if cur_node in group_mapping and group != group_mapping[cur_node]: # check if it's confilict
                        return False
                    if cur_node in visited: continue    # If visited and no conflict, continue to avoid dead loop
                    group_mapping[cur_node] = group     # Assign group for current node
                    visited.add(cur_node)
                    for child in self.graph[cur_node]:  # Assign contray group for dislikes of current node
                        tmp_stack.append((child, not group))
        return True

n = 4
dislikes = [[1,2],[1,3],[2,4]]
print(S().possibleBipartition(n, dislikes))



# https://leetcode.com/problems/possible-bipartition/discuss/655842/python-union-find-dfs-bfs-with-explanation