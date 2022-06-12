
from typing import List

class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums }

        print(strSet)

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in strSet else res

            res = backtrack(i + 1, cur)
            if res: return res

            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res: return res

        return backtrack(0, ["0" for s in nums])




print(Solution().findDifferentBinaryString(["01", "10"]))

# https://leetcode.com/problems/find-unique-binary-string/
# https://www.youtube.com/watch?v=aHqn4Dynd1k&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=12&ab_channel=NeetCode
