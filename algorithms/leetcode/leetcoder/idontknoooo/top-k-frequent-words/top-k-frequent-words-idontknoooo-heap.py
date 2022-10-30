'''
https://leetcode.com/problems/top-k-frequent-words/

https://leetcode.com/problems/top-k-frequent-words/discuss/2078298/python3-onlogk-heap-customized-string-explanation

Approach 2. Heap + Customized String
For the same frequencies, we want to keep the word with lower lexicographical order
In a Python heap (minheap), it's easy to keep track of top k of something, but to keep track of bottom k, we will need a maxheap
    It's easy to turn integer to adapt to a maxheap by giving it an minus - sign
    But for string, we can't, thus, we will need to find a way to do it for string
    There are multiple ways of doing it, in this solution, we will create our own string class MyStr and overwrite comparators __lt__ & __gt__
With below MyStr, we can make sure that
    frequency is stored as if it's in a minheap (to eliminate the lowest)
    word is stored as if it's in a maxheap (to eliminate highest)
Time: dominate by O(NlogK), N = len(words)

'''
import collections
from typing import List
import heapq

class MyStr(str):

    def __init__(self, val):
        self.val = val

    def __lt__(self, s):
        return self.val > s.val

    def __gt__(self, s):
        return self.val < s.val

class S:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        c = collections.Counter(words)      # O(n)
        cnt, heap = 0, []
        for word, v in c.items():           # worst case O(n)
            word = MyStr(word)
            if cnt < k:                     # O(logk)
                heapq.heappush(heap, (v, word))
                cnt += 1
            elif cnt == k and ( \
                    v > heap[0][0] or \
                    v == heap[0][0] and word > heap[0][1]):
                heapq.heappop(heap)
                heapq.heappush(heap, (v, word))
        ans = []
        while heap:                         # O(klogk)
            ans.append(heapq.heappop(heap)[1])
        return ans[::-1]                    # O(k)

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4

print(S().topKFrequent(words, k))
