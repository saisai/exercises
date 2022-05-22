
import collections

class UF:

    def __init__(self, n):
        self.p = [i for i in range(n+1)]

    def find(self, i):      # Find parent
        if i != self.p[i]:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, j, parent_dislike_i, parent_i):
        p_j = self.find(j)
        self.p[p_j] = parent_dislike_i
        return p_j != parent_i      # check if there is a parent conflict


class S:
    def possibleBipartition(self, N, dislikes):
        self.graph = collections.defaultdict(list)  # Create graph and initilize union find
        uf = UF(N)
        for (u, v) in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)

        for i in range(1, N+1):
            parent_i = uf.find(i)
            if parent_i in self.graph:
                parent_dislike_i = uf.find(self.graph[i][0])  # Pick a dislike node's parent as a common parent for the rest of dislike nodes
                for dis in self.graph[i][1:]:       # For each dislike node
                    if dis < i: continue            # This line is optional, it speeds things up
                    if not uf.union(dis, parent_dislike_i, parent_i): return False # Return Flase if thereis a conflict when grouping
        return True
n = 4
dislikes = [[1,2],[1,3],[2,4]]
print(S().possibleBipartition(n, dislikes))

# https://leetcode.com/problems/possible-bipartition/discuss/655842/python-union-find-dfs-bfs-with-explanation
