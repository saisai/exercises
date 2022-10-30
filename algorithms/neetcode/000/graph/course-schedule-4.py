from collections import deque

class S:

    @classmethod
    def canFinish(cls, numCoureses, prerequisites):
        '''
        solution approach:
        1. create the adjacency list from given edges
        2. for each node, traverse graph starting at this node (BFS/DFS);
            if we detect a loop, return False
        3. return True
        '''

        # create adjancey list
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
            #graph[b].append(a) # no because graph is directional!

        for n in range(0, numCourses):
            Q = deque(graph[n])
            visited = set()
            while Q:
                m = Q.popleft() # --> BFS
                #m = Q.pop()    # --> DFS
                if m == n:
                    # we detected a loop
                    return False
                visited.add(m)  # this is just for optimization, not strictyl needed
                for neighbor in graph[m]:
                    if neighbor not in visited:
                        Q.append(neighbor)
        return True


numCourses = 2
prerequisites = [[1,0]]
print(S.canFinish(numCourses, prerequisites))

