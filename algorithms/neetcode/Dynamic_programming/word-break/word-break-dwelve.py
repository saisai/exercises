'''
Simple iterative BFS or DFS. 24 to 32 ms (Python 3, Nov 2019).

Starts with string s. For each string visited, chop off front of string if it starts with a word in the dictionary and adds the shortened string to the queue or stack. If string becomes empty, that means word break succeeded. Keep a set of seen string states to avoid duplicate work.

https://leetcode.com/problems/word-break/discuss/428606/Python-Simple-Iterative-BFS-or-DFS-24ms

https://leetcode.com/problems/word-break/
'''

class S:

    def wordBreak(self, s, wordDict):
        from collections import deque

        q = deque([s])
        seen = set()
        while q:
            s = q.popleft() # popleft() = BFS; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "":
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False

s = "leetcode"
wordDict = ["leet","code"]
print(S().wordBreak(s, wordDict))
