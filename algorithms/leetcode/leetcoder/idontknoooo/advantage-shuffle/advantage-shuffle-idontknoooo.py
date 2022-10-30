'''
https://leetcode.com/problems/advantage-shuffle/
https://leetcode.com/problems/advantage-shuffle/solutions/843628/python-3-greedy-two-pointers-explana/

Explanation
Intuitively, we can see that, for A, to make the most advantage over B is to use large number cover large number, small number to cover small number, if possible. e.g.
    A = [5, 9], B = [4, 8], we can easily tell, 5 covers 4, 9 covers 8
    but if we switch the order, we noticed that 9 covers 4, but 5 can't cover 8
Given the thought above, we simply sort A & B (reversely, from large to small)
Iterate over B,
    if current A[j] covers current B[i]
        we take it, meaning assign A[j] at the original index (ori_idx) of B[i]
        then increment j, meaning use next largest number in A
    otherwise, meaning B[i] is too large for the current maximum available A[j], so check whether next number (B[i+1]) can be covered by A[j]
After we iterate over B, there might have some original index wasn't assigned (because it's possible that not all values is B was covered)
    Simply iterate over ans, if we meet a -1 (meaning wasn't assigned), then assign the rest value in A to them 
Implementation
'''
from typing import List

class S:

    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sorted_a = sorted(A, reverse=True)                                          # # descending order
        sorted_b = sorted(enumerate(B), key=lambda x: (x[1], x[0]), reverse=True)   # descending order with original index
        n, j = len(B), 0
        ans = [-1] * n
        for i, (ori_idx, val) in enumerate(sorted_b):                               # A greedily tries to cover value in B as large as possible
            if sorted_a[j] > val: ans[ori_idx], j = sorted_a[j], j+ 1
        for i in range(n):
            if ans[i] == -1: ans[i], j = sorted_a[j], j + 1
        return ans

nums1 = [2,7,11,15]
nums2 = [1,10,4,11]
print(S().advantageCount(nums1, nums2))
