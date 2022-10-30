'''

https://www.youtube.com/watch?v=XYQecbcd6_c&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=7&ab_channel=NeetCode

https://leetcode.com/problems/longest-palindromic-substring/
'''

class S:

    def longestPalindrome(self, s: str) -> str:

        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r -l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = s - l + 1
            l -= 1
            r += 1
        return res

s = "babad"
print(S().longestPalindrome(s))
