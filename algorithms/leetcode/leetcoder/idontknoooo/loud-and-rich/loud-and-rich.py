
'''
https://leetcode.com/problems/loud-and-rich/
https://leetcode.com/problems/loud-and-rich/solutions/782931/python-3-dfs-memoization-lru_cache/

First, we make a graph with dictionary, where key is person x and values are those who is richer than x (list of people).

Second, we do a DFS and at the same time lru_cache will take care of the repeat input of any person i

cur: current quiet level

r: current rich people who is least quiet
'''
from typing import List
from functools import lru_cache
import collections

class S:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = collections.defaultdict(list)
        for x, y in richer: graph[y].append(x)
        #print(graph)

        @lru_cache(maxsize=None)
        def dfs(i):
            cur, r = quiet[i], i
            if i not in graph: return cur, r
            for rich in graph[i]:
                cur1, r1 = dfs(rich)
                if cur1 < cur:
                    cur, r = cur1, r1
            return cur, r
        #return [dfs(i)[1] for i in range(len(quiet))]
        result = []
        for i in range(len(quiet)):
            result.append(dfs(i)[1])
        print(result)
        return result

richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(S().loudAndRich(richer, quiet))
