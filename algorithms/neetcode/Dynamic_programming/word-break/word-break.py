'''

https://www.youtube.com/watch?v=Sx9NNgInc3A&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=6&ab_channel=NeetCode

https://leetcode.com/problems/word-break/
'''

class S:

    def wordBreak(self, s, wordDict):

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        print(dp)

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        print(dp)
        return dp[0]

s = "leetcode"
wordDict = ["leet","code"]
print(S().wordBreak(s, wordDict))
