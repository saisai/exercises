'''
https://leetcode.com/problems/longest-palindromic-subsequence/discuss/1082918/python-dp-with-two-pointers
https://leetcode.com/problems/longest-palindromic-subsequence/
'''
import functools

class S:

    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        optimized break-down of the problem,
            with less memory consumption, as well as less computation.
        '''

        @functools.lru_cache(maxsize=None)
        def dp(left, right):

            if left == right:
                return 1
            elif left > right:
                return 0

            if s[left] == s[right]:
                return 2 + dp(left+1, right-1)
            else:
                return max(dp(left+1, right), dp(left, right-

                    1))
        return dp(0, len(s) - 1)

s = "bbbab"
print(S().longestPalindromeSubseq(s))
