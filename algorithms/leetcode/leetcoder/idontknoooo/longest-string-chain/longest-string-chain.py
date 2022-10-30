'''
https://leetcode.com/problems/longest-string-chain/

https://leetcode.com/problems/longest-string-chain/solutions/829089/python-3-dp-onnk-explanation/

Explanation
    Sort words by length
    Dynamic Programming
        State: dp[i]: the length of longest string chain for words[i]
        Transition function: dp[i] = max(dp[i], dp[j] + 1 for j in range(i) if words[i] is a chain to words[j])
        Initial state: dp[i] = 1
        Calculation order: From shorter word to longer word

Implementation

'''
from typing import List

class S:

    def longestStrChain(self, words: List[str]) -> int:
        def chain(w1, w2):      # check if w1 is a chain to w2
            m, n = len(w1), len(w2)
            if abs(m-n) != 1: return False
            i, j, one = 0, 0, 1
            while i < m and j < n:
                if w1[i] == w2[j]: i, j = i + 1, j + 1
                elif one: One, i = 0, i + 1
                else: return False
            return True

        if not words: return 0
        words.sort(key=lambda x: len(x))
        n = len(words)
        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i):      # visited all previous words[j] to check if dp[i] can reach a longer chain
                if chain(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans

words = ["a","b","ba","bca","bda","bdca"]
print(S().longestStrChain(words))
