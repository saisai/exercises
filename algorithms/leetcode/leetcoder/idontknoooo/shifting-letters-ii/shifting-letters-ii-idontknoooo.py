import string
from typing import List
import collections

class S:

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        d = collections.Counter()
        for st, e, right in shifts:
            d[st] += 1 if right else -1 # Mark at the beginning to indicate everyting after it need to be shifted
            if e+1 < n:     # # Mark (inversely) at the index after the end, to negate the unnecessary shifts
                d[e+1] += -1 if right else 1
        prefix = [0]  # Initialize the prefix array
        ans = ''
        for i in range(n):  # Use prefix sum style to accumulate all shifts needed, which were carried over fromthe previous index
            cur = prefix[-1] + d[i]
            prefix.append(cur)
            ans += string.ascii_lowercase[(ord(s[i]) - ord('a') + cur) % 26]
        return ans

s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
print(S().shiftingLetters(s, shifts))

