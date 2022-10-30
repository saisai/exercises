'''
https://leetcode.com/problems/flip-string-to-monotone-increasing/
https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/1395710/python-3-prefixsuffix-two-pass-explanation

Explanation
    Intuition is that the ultimate string will be either
        '000....0000'
        '111....1111'
        '000....1111'
    Basically, the final string will have only '0' on the left of some index i and have only '1' on the right of it
    What we need to do is to assume any index among 0 to n-1 can be the special index i, then count how many '1' will be flipped to '0' on its left and how many '0' will be flipped to '1' on its right.
    In a new loop, we add them together and find the minimum as the answer
    Don't forget to count 2 special cases (all zeros or all ones)

Implementation
'''

import sys

class S:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zero, one = [0] * n, [0] * n
        prefix = suffix = 0
        for i in range(n):
            if s[i] == '1':
                prefix += 1
            zero[i] = prefix # flip '1' to '0
            if s[n-1-i] == '0':
                suffix += 1
            one[n-1-i] = suffix # flip '0' to '1' (from right to left)

        ans = sys.maxsize
        for i in range(n - 1):
            ans = min(ans, zero[i] + one[i+1]) # `i` and its left are all '0' and '1's are on its right
        else:
            ans = min(ans, zero[n-1], one[0]) # zero[n-1] -> all zeros, one[0] -> all cones
        return ans


s = "00110"
print(S().minFlipsMonoIncr(s))
