'''

https://leetcode.com/problems/word-break/discuss/43788/4-lines-in-Python
https://leetcode.com/problems/word-break/
'''

class S:

    def wordBreak(self, s, words):

        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]


s = "leetcode"
wordDict = ["leet","code"]
print(S().wordBreak(s, wordDict))
