'''
https://leetcode.com/problems/maximum-split-of-positive-even-integers/

https://leetcode.com/problems/maximum-split-of-positive-even-integers/discuss/1784492/python-3-math-explanation
Explanation
    We want the number series grow as slow as possible. One way is to use sum of an Arithmetic Sequence.
Implementation
'''
from math import sqrt
from typing import List

class S:

    def maximumEvenSplit(self, finalSum: int) -> List[int]:

        if finalSum % 2: return []
        value = int(sqrt(finalSum))
        ans = [2 * i for i in range(1, value)]
        diff = finalSum - sum(ans)
        if ans and diff <= ans[-1]:
            return ans[:-1] + [diff + ans[-1]]
        else:
            return ans + [diff]

finalSum = 12
print(S().maximumEvenSplit(finalSum))
