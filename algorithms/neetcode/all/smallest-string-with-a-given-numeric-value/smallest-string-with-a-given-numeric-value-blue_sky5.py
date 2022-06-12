
''''
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/discuss/2135418/python-greedy-from-the-back
'''
from typing import List
import string

class S:

    def getSmallestString(self, n: int, k: int) -> str:

        char = {i + 1: c for i, c in enumerate(string.ascii_lowercase)}
        print(char)
        result = ['a'] * n
        print(result)
        idx = n - 1
        to_assign = k - n
        while to_assign > 0:
            value = min(25, to_assign)
            result[idx] = char[value+1]
            to_assign -= value
            idx -= 1
        print(result)
        return "".join(result)

n = 3
k = 27
print(S().getSmallestString(n, k))
