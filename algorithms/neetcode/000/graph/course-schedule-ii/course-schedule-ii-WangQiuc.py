'''
A regular topological sort problem. A good case for practice.

The first approach is BFS and we build the topological order in order: each time we put the node with 0 indegree at the front of the remaining sequence.

We need to maintain two graphes: dst sets edges as source->destination while the src sets edges as destination->source.

For our sorted array, each time we append the node which has no sources (src indegree is 0) to it. And each time we pick one node in sorted array (ganranteed that all of its prerequisite nodes are sorted in front of it so none of rest nodes are its prerequisites) and check its destination nodes(children node in dst). Then we "remove" it as a prerequsite from its destination nodes by decreasing all those destination nodes' indegree by 1. Once any of those destination nodes has 0 indegree, we can put them into the sorted array.

Besides, if there is a cycle in it, then schedule is not arrangable so we should return [].
In such case, those nodes in the cycle will always has at least a source node (also in that cycle) so they will never be appended in the sorted array. After we finished our serach, if sorted array's size is less than number of courses, then there is a cycle it it.

https://leetcode.com/problems/course-schedule-ii/
'''
from typing import List
import collections

class S:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        src, dst = collections.Counter(), [set() for _ in range(numCourses)]
        for d, s in prerequisites:
            src[d] += 1
            dst[s].add(d)
        ans = [x for x in range(numCourses) if not src[x]]
        for s in ans:
            for d in dst[s]:
                src[d] -= 1
                if not src[d]:
                    ans.append(d)
        return ans if len(ans) == numCourses else []


numCourses = 2
prerequisites = [[1,0]]

print(S().findOrder(numCourses, prerequisites))

