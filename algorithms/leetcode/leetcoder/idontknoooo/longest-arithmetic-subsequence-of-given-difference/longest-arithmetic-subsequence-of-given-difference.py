'''
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/solutions/822287/python-3-one-pass-dp-dictionary/
'''
import collections
from typing import List

class S:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d, ans = collections.defaultdict(int), 0
        for num in arr:
            d[num] = d[num-difference] + 1
            ans = max(ans, d[num])
        return ans

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(S().longestSubsequence(arr, difference))
