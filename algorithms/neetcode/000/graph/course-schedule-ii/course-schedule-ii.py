'''
https://www.youtube.com/watch?v=Akt3glAwyfY&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=4&ab_channel=NeetCode

https://leetcode.com/problems/course-schedule-ii/
'''
from typing import List

class S:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build adjacency list of prepres
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

numCourses = 2
prerequisites = [[1,0]]

print(S().findOrder(numCourses, prerequisites))

