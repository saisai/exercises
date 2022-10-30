'''

https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/solutions/855405/python-3-backtracking-dfs-clean-explanations/

Explanation
    The length of s is only up to 16, so it won't hurt if we exhaustively try out all possibility
    And intuitively backtracking + DFS is very good at doing job like this
    Check comment for more detail, pretty standard backtracking problem
Implementation
'''
class S:

    def maxUniqueSplit(self, s: str) -> int:
        ans, n = 0, len(s)
        def dfs(i, cnt, visited):
            nonlocal ans, n
            if i == n: ans = max(ans, cnt); return  # stop condition
            for j in range(i+1, n+1):
                if s[i:j] in visited: continue      # avoid re-visit/dulicates
                visited.add(s[i:j])                 # update visited set
                dfs(j, cnt+ 1, visited)             # backtracking
                visited.remove(s[i:j])              # recover visited set for next possiblity

        dfs(0, 0, set())                            # function call

        return ans

s = "ababccc"
print(S().maxUniqueSplit(s))
