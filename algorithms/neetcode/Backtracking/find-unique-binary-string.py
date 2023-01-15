
from typing import List

class S:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = { s for s in nums }
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
nums = ["01","10"]
nums = ["00","01"]
print(S().findDifferentBinaryString(nums))
