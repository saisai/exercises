
"""

https://leetcode.com/problems/longest-common-subsequence/
https://leetcode.com/problems/longest-common-subsequence/discuss/350993/Python-dp-and-recursive

dp(i,j) means the longest common subsequence of text1[:i] and text2[:j].
If text1[i]==text2[j], then dp(i,j) should equal dp(i-1,j-1)+1
Otherwise, dp(i,j)=max(dp(i-1,j), dp(i,j-1))

Both dp and recursive version can be constructed based on the above idea.

"""

from typing import List

class S:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]


text1 = "abcde"
text2 = "ace" 
print(S().longestCommonSubsequence(text1, text2))
