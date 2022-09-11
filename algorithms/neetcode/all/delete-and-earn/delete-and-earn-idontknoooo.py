'''
https://leetcode.com/problems/delete-and-earn
https://leetcode.com/problems/delete-and-earn/discuss/1820848/python-3-dp-greedy-onlogn-house-robber-explanation

Explanation
    This is essentially a variation of 198. House Robber.
    You don't want to pick neighbor, but you want keep the one before that.
    Keep a current (cur) and a previous value (prev)
        If the previous number is a neighbor (i.e. keys[i] == keys[i-1] + 1), then update current with the maximum between cur and prev + keys[i] * c[keys[i]]
        If not neighbor, then you can update current with cur + keys[i] * c[keys[i]]

Implementation
'''
import collections

from typing import List

class S:

    def deleteAndEarn(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        keys = sorted(c.keys())
        prev = 0
        ans = cur = c[keys[0]] * keys[0]
        for i in range(1, len(keys)):
            if keys[i] == keys[i-1] + 1:
                prev, cur = cur, max(cur, prev + keys[i] * c[keys[i]])
            else:
                prev, cur = cur, cur + keys[i] * c[keys[i]]
            ans = max(ans, cur)
        return ans


for nums in [[3, 4, 2], [2,2,3,3,3,4]]:
    print(S().deleteAndEarn(nums))
