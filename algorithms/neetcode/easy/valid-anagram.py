
from collections import Counter

class S:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)

        return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

s = "anagram"
t = "nagaram"

print(S().isAnagram(s, t))