'''
https://leetcode.com/problems/remove-stones-to-minimize-the-total/

https://leetcode.com/problems/remove-stones-to-minimize-the-total/discuss/1390561/python-3-heap-explanation
Explanation
    Always pick the maximum number to reduce
    Use a max-heap to help
    
Implementation

'''

import heapq

from typing import List

class S:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        print(heap)
        heapq.heapify(heap)
        print(heap)
        for _ in range(k):
            cur = -heapq.heappop(heap)
            heapq.heappush(heap, -(cur-cur//2))
        print(heap)
        return -sum(heap)

piles = [5,4,9]
k = 2

print(S().minStoneSum(piles, k))

