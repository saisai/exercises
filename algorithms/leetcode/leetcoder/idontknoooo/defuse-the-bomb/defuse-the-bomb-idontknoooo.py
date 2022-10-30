'''
https://leetcode.com/problems/defuse-the-bomb/
https://leetcode.com/problems/defuse-the-bomb/discuss/935556/python-3-5-line-on-explanation

Explanation
Prefix sum on circular array
Create a prefix sum array with length of 2*l, where l is the length of code; in this way, we get rid of concerns about circulation; this is a classic technique to handle circular array
Take prefix sum and get K sum accordingly, depending on k
Implementation


'''
from typing import List

class S:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)
        if not k: return [0] * l
        pre_sum = [0] * (2*l)
        for i in range(2*l): pre_sum[i] = pre_sum[i-1] + code[i%l]
        return [pre_sum[k+i] - pre_sum[i] if k > 0 else pre_sum[i+l-1] - pre_sum[k+i+l-1] for i in range(l)]


code = [5,7,1,4]
k = 3

print(S().decrypt(code, 3))

