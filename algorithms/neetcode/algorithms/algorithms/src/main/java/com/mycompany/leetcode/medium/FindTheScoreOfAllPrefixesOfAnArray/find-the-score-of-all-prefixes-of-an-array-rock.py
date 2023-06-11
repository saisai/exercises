
from typing import List

class S:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        score, mx = [0], 0
        for num in nums:
            mx = max(mx, num)
            score.append(score[-1] + num + num)
        return score[1:]

nums = [2,3,7,5,10]
print(S().findPrefixScore(nums))