
class S:
    def canFinish(self, n, prerequisites):
        graph = [[] for _ in range(n)]
        visit = [0 for _ in range(n)]
        print(graph)
        print(visit)
        for x, y in prerequisites:
            graph[x].append(y)
        print(graph)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(n):
            if not dfs(i):
                return False
        return True


numCourses = 2
prerequisites = [[1,0]]
print(S().canFinish(numCourses, prerequisites))
