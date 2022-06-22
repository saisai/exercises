
"""
https://leetcode.com/problems/longest-common-subsequence/discuss/350993/Python-dp-and-recursive
https://leetcode.com/problems/longest-common-subsequence/

"""
import functools
from typing import List

class S:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @functools.lru_cache(None)
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return helper(i-1, j-1) + 1
            return max(helper(i-1, j), helper(i, j-1))
        return helper(len(text1) - 1, len(text2) -1 )


text1 = "abcde"
text2 = "ace" 
print(S().longestCommonSubsequence(text1, text2))
