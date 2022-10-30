'''
https://leetcode.com/problems/word-break/
https://www.youtube.com/watch?v=Sx9NNgInc3A&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=19&ab_channel=NeetCode

'''
from typing import List

class S:

    def wordBreak(self,s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

s = "leetcode"
wordDict = ["leet","code"]
print(S().wordBreak(s, wordDict))
