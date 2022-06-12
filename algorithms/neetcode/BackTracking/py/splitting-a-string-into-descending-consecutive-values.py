import pdb

class Solution:
    def __call__(self, s):
        def dfs(index, prev):
            pdb.set_trace()
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val = int(s[index:j + 1])
                if val + 1 == prev and dfs(j +1, val):
                    return True
            return False
        for i in range(len(s) - 1):
            val = int(s[:i+1])
            if dfs(i + 1, val): return True
        return False

#print(Solution()('050043'))
print(Solution()('9080701'))

# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
# https://www.youtube.com/watch?v=eDtMmysldaw&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=7&ab_channel=NeetCode