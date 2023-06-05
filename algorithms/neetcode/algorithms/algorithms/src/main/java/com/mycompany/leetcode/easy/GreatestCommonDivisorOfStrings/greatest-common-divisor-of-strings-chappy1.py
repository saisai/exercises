
from math import gcd

class S:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)
        val = gcd(str1_len, str2_len)
        
        if str1[:val] == str2[:val] and ((str1 + str2) == (str2+str1)):
            return str1[:val]
        else:
            return ""
        
str1 = "ABCABC"
str2 = "ABC"
print(S().gcdOfStrings(str1, str2))