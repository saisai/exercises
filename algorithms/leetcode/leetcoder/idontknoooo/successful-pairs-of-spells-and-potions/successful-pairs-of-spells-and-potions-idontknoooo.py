'''
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

https://leetcode.com/problems/successful-pairs-of-spells-and-potions/discuss/2139547/python-3-math-binary-search-explanation

Explanation
The order of potions doesn't matter, we just need to find out how many potion can form a successful pair with the current spell
    Thus, we can sort potions to make a faster binary search
We can't use spell to multiply each potion, it takes a long time O(mn);
    Instead, we can use success to divided by the current spell, which is a O(1) operation
If success % spell == 0, then we want to include success // spell
    Thus, we will use a bisect_left
Otherwise, we don't want to include success // spell
    Thus, we will use a bisect_right
n - idx is the number of successful potions with the current spell
Time: O(nlgm), n = len(spells), m = len(potions)

'''
import bisect

from typing import List

class S:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        ans, n = [], len(potions)
        for spell in spells:
            val = success // spell
            if success % spell == 0:
                idx = bisect.bisect_left(potions, val)
            else:
                idx = bisect.bisect_right(potions, val)
            ans.append(n - idx)
        return ans

spells = [3,1,2]
potions = [8,5,8]
success = 16
print(S().successfulPairs(spells, potions, success))
