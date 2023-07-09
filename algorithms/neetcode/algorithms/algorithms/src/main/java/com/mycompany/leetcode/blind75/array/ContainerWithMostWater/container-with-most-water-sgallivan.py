
from typing import List

class S:
    def maxArea(self, H: List[int]) -> int:
        ans, i, j = 0, 0, len(H) - 1
        while i < j:
            if H[i] <= H[j]:
                res = H[i] * (j - i)
                i += 1
            else:
                res = H[j] * (j - i)
                j -= 1
            if res > ans: ans = res
        return ans 

height = [1,8,6,2,5,4,8,3,7]
print(S().maxArea(height))