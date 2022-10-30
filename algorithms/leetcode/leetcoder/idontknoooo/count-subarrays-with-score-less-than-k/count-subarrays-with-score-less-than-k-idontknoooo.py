'''

https://leetcode.com/problems/count-subarrays-with-score-less-than-k/discuss/2140147/python-3-sliding-window-two-pointers-math-explanation
https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

Explanation
The key is to append a very large value to the end of the list, in this case k is enough
slow: Slow pointer
i: Fast pointer
cur: Current prefix sum
ans: Answer
When cur * (i - slow + 1) >= k, then there are i - slow subarrays satisfy the condition
    Each subarray starts from slow, end at each j where slow <= j < i
Time: O(N), N = len(nums)
Implementation

'''
from typing import List

class S:

    def countSubarrays(self, nums: List[int], k: int) -> int:

        nums += [k]
        slow = cur = ans = 0
        for i, num in enumerate(nums):
            cur += num
            while cur * (i - slow + 1) >= k:
                ans += i - slow
                cur -= nums[slow]
                slow += 1
        return ans

nums = [2,1,4,3,5]
k = 10
print(S().countSubarrays(nums, k))

