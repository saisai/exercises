'''
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/discuss/1439073/python-3-on-explanation

Python 3 | O(N) | Explanation

Mod the total sum of chalk, so that k can be exhaust in one iteration
Then, iterate over chalk to find student i

'''

from typing import List

class S:

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, num in enumerate(chalk):
            if k >= num: k -= num
            else: return i
        return -1

chalk = [5,1,5]
k = 22
print(S().chalkReplacer(chalk, k))
