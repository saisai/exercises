'''
https://leetcode.com/problems/friends-of-appropriate-ages/
https://leetcode.com/problems/friends-of-appropriate-ages/discuss/2074946/python-3-three-methods-binary-search-counterhashmap-math-explanation

Approach 2. Counter + Nested loop
    Time complexity: max(O(121*121), N), N = len(ages)
'''

import bisect


from typing import List

class S:

    def numFriendRequests(self, ages: List[int]) -> int:

        count = [0] * 121 # couner: count frequency of each age
        for age in ages:
            count[age] += 1
            
        ans = 0
        for ageA, countA in enumerate(count): # nested loop, pretty straightforward
            
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans

ages = [16,17,18]
print(S().numFriendRequests(ages))
