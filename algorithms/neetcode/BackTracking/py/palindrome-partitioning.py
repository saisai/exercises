import pdb
from typing import List

class Solution:
    def partition(self, ss: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            pdb.set_trace()
            if i >= len(ss):
                res.append(part[:])
                #res.append(part.copy())
                return
            for jj in range(i, len(ss)):
                if self.isPali(ss, i, jj):
                    part.append(ss[i:jj+1])
                    dfs(jj+1)
                    part.pop()
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:

            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
print(Solution().partition("aab"))


# https://www.youtube.com/watch?v=3jvWodd7ht0&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=5&ab_channel=NeetCode
# https://leetcode.com/problems/palindrome-partitioning/
