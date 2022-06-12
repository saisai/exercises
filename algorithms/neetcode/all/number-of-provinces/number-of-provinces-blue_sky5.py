
'''
Python, DFS modifying the array

https://leetcode.com/problems/number-of-provinces/discuss/2136147/python-dfs-modifying-the-array
https://leetcode.com/problems/number-of-provinces/
'''
from typing import List

class S:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city):
            isConnected[city][city] = 0
            for c in range(n):
                if isConnected[city][c]:
                    isConnected[city][c] = 0
                    isConnected[c][city] = 0
                    dfs(c)
        result = 0
        n = len(isConnected)
        for city in range(n):
            if isConnected[city][city]:
                result += 1
                dfs(city)
        return result

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(S().findCircleNum(isConnected))
