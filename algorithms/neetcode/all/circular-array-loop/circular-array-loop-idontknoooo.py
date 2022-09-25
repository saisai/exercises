'''

Explanation
    Not the most efficient solution, but it's one of the cleanest
    Time: O(n), Space O(n)
    Note: The starting index can be any index, NOT zero only
    Take each unvisited index and start traverse, mark as visited at the meantime
    If sign changes or cycle at itself, break the loop; otherwise, if revisited an index, return True
Implementation

https://leetcode.com/problems/circular-array-loop/
https://leetcode.com/problems/circular-array-loop/discuss/1317119/python-3-short-python-set-explanation

'''
from typing import List


class S:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n, visited = len(nums), set()
        for i in range(n):
            if i not in visited:
                local_s = set()
                while True:
                    if i in local_s: return True
                    if i in visited:  break # credit to @crazyhyz, add this condition to avoid revisited
                    visited.add(i)
                    local_s.add(i)
                    prev, i = i, (i + nums[i]) % n
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0): break
        return False

nums = [2,-1,1,2,2]
print(S().circularArrayLoop(nums))

