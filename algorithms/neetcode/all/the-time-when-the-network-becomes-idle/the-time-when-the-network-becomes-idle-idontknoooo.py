'''
https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

Explanation
Only thing we need to know is the shortest distance between current node and master node
Find the maximum among all data nodes, then we will get the answer
See explanation below
https://leetcode.com/problems/the-time-when-the-network-becomes-idle/discuss/1531159/python-3-clean-bfs-deque-explanation


'''

import collections

class S:
    def networkBecomesIdle(self, edges, patience):
        graph = collections.defaultdict(list)
        for a, b in edges:      # build a graph
            graph[a].append(b)
            graph[b].append(a)
        dq = collections.deque([(0, 0)])            # prepare bfs using queue
        ans, n = 0, 1
        visited = set()
        while dq:
            for _ in range(n):
                cur, step = dq.popleft()
                n -= 1                      # key track of size of dq
                visited.add(cur)
                for nei in graph[cur]:
                    if nei in visited: continue
                    visited.add(nei)
                    n += 1
                    dq.append((nei, step+1))
                if cur:
                    time = step * 2         # first msg round trip time
                    mod = time % patience[cur]
                    finished = patience[cur] if not mod else mod # last msg finished moves
                    total = time + (time - finished) # total time = time + last_msg_unifinised_moves
                    ans = max(ans, total)
        return ans + 1

edges = [[0,1],[1,2]]
patience = [0,2,1]
print(S().networkBecomesIdle(edges, patience))
                            
