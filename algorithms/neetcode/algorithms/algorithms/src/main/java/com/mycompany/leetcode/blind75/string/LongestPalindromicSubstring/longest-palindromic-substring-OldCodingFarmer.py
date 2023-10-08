
class S:

    def longestPalindrome(self, s):

        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp

            # even case , like "abba"
            tmp = helper(s, i, i +1)
            if len(tmp) > len(res):
                res = tmp

        return res 

s = "babad"
print(S().longestPalindrome(s))
