'''
https://leetcode.com/problems/valid-square/

https://leetcode.com/problems/valid-square/solutions/827796/python-3-pythagoras-theorem-explanation/

'''

from typing import List
import collections

class S:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if not p1 != p2 != p3 != p4: return False       # 4 points have to be different
        dis = lambda x, y: (y[1]-x[1])**2 + (y[0]-x[0])**2  # lambda function to calc distance**2
        points = [p1, p2, p3, p4]
        d = collections.defaultdict(list)
        for i in range(4):
            for j in range(i+1, 4):
                distance = dis(points[i], points[j])
                d[tuple(points[i])].append(distance)
                d[tuple(points[j])].append(distance)
        for point, distances in d.items():      # check neighbour edges equality & Pythagoras theorem
            distances.sort()
            if not (distances[0] == distances[1] and sum(distances[:2]) == distances[2]): return False
        return True


p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

print(S().validSquare(p1, p2, p3, p4))

