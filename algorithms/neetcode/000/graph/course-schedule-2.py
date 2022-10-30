
from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        return stack[::-1]

class S:

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = Graph(numCourses)
        for coursePair in prerequisites:
            g.addEdge(coursePair[1], coursePair[0])
        sortedCourses = list(g.topologicalSort())
        result = True
        for coursePair in prerequisites:
            if sortedCourses.index(coursePair[1]) >= sortedCourses.index(coursePair[0]):
                result = False
        return result


numCourses = 2
prerequisites = [[1,0]]

print(S().canFinish(numCourses, prerequisites))

