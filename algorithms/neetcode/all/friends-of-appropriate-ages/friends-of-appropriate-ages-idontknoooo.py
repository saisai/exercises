'''
https://leetcode.com/problems/friends-of-appropriate-ages/
https://leetcode.com/problems/friends-of-appropriate-ages/discuss/2074946/python-3-three-methods-binary-search-counterhashmap-math-explanation

Approach 1. Binary Search + Math
    Time Complexity: O(NlogN), N = len(ages)
'''

import bisect


from typing import List

class S:

    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort() # sort the ages
        ans = 0
        n = len(ages)
        for idx, age in enumerate(ages): # for each age
            lb = age # lower bound
            ub = (age - 7) * 2 # upper bound
            i = bisect.bisect_left(ages, lb) # binary search lower bound
            j = bisect.bisect_left(ages, ub) # binary search upper  bound
            if j -i <= 0: continue
            ans += j - i        # count number of potential friends
            if lb <= age < ub: # ignore itself
                ans -= 1
        return ans

ages = [16,17,18]
print(S().numFriendRequests(ages))
