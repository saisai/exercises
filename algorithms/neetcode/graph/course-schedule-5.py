class S:

    def canFinish(self, numCourses, prerequisites):

        preMap = { i: [] for i in range(numCourses)}
        visitedSet = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visitedSet:
                return False
            if preMap[crs] == []:
                return True

            visitedSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visitedSet.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

numCourses = 2
prerequisites = [[1,0]]

print(S().canFinish(numCourses, prerequisites))

