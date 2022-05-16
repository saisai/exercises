from collections import defaultdict, deque


class S:

    def canFinish(self, numCourses, prerequisites):
        adj_list = defaultdict(list)
        indegrees = [0] * numCourses

        for i, j in prerequisites:
            adj_list[j].append(i)
            indegrees[i] += 1

        q = deque()

        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)

        topo_count = 0


        while q:
            node = q.popleft()
            topo_count += 1
            for child in adj_list[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)

        return True if topo_count == numCourses else False
    

numCourses = 2
prerequisites = [[1,0]]

print(S().canFinish(numCourses, prerequisites))

