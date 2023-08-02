from functools import lru_cache

class S:
    def wordBreak(self, s, wrodDict):
        wordSet = set(wrodDict)
        n = len(s)
        
        @lru_cache(None)
        def dfs(k):
            if k== n: return True
            for i in range(k + 1, n + 1):
                if s[k:i] in wordSet and dfs(i):
                    return True
            return False
        
        return dfs(0)

s = "leetcode"
wordDict = ["leet","code"]
print(S().wordBreak(s, wordDict))