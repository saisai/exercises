'''
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/1428517/python-3-hash-table-bitmask-tuple-on-two-implementations-explanation

Approach #2 Bitmasking
    As you can see, this method is essentially the same as the previous
    From time complexity perspective, both are O(N), where N is the length of s
    However, with bit manipulation, the performance of this method will be slightly better than approach #1
'''

import sys

import collections

class S:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {0: -1}
        ans = cur = 0
        vowel = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        for i, c in enumerate(s):
            if c in vowel:
                cur ^= 1 << vowel[c]
                print(cur)
            if cur not in d:
                d[cur] = i
                print("dd ", d)
            ans = max(ans, i - d[cur])
        return ans

s = "eleetminicoworoep"
print(S().findTheLongestSubstring(s))

