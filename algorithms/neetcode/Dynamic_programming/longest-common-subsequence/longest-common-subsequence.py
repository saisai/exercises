
"""

https://www.youtube.com/watch?v=Ua0GhsJSlWM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=14&ab_channel=NeetCode
https://leetcode.com/problems/longest-common-subsequence/

"""

from typing import List

class S:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]

text1 = "abcde"
text2 = "ace" 
print(S().longestCommonSubsequence(text1, text2))
