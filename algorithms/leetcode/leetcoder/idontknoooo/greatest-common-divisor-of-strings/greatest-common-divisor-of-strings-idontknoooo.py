'''
https://leetcode.com/problems/greatest-common-divisor-of-strings/
https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/860984/python-3-gcd-1-liner-explanation/

To have GCD substring, the length of it has to be a GCD of len(s1) and len(s2)
Check if s1 + s2 == s2 + s1 to make sure such a string exists
'''
import math

class S:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        return s1[:math.gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ''

str1 = "ABCABC"
str2 = "ABC"
print(S().gcdOfStrings(str1, str2))

