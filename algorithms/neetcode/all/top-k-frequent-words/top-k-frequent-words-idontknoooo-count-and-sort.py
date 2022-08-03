'''

Approach 1. Count & Sort
Time: Worst case O(NlogN), N = len(words)

https://leetcode.com/problems/top-k-frequent-words/discuss/2078298/python3-onlogk-heap-customized-string-explanation

https://leetcode.com/problems/top-k-frequent-words/
'''
from typing import List
import collections

class S:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        return [x[0] for x in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:k]]

words = ["i","love","leetcode","i","love","coding"]
k = 2
print(S().topKFrequent(words, k))
