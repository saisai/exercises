'''
https://leetcode.com/problems/course-schedule/
https://www.youtube.com/watch?v=EgI5nU9etnU&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=3&ab_channel=NeetCode
'''
from typing import List

class S:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = { i: [] for i in range(numCourses) }
        print(preMap)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)

        # visitSet = all coureses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


numCourses = 2
prerequisites = [[1,0]]
print(S().canFinish(numCourses, prerequisites))
