
''''

(Note: This is part of a series of Leetcode solution explanations (index). If you like this solution or find it useful, please upvote this post.)

Idea:

The basic idea is simple: in order for the string to be as lexigraphically "small" as it can be, you want to move as much of the "weight" towards the rear of the string as possible.

That means you want as many "z"s at the end of the answer and as many "a"s at the beginning of the answer as you can get. This also means that there will only be at most one character that is neither an "a" or a "z".

First, remove n from k in order to leave yourself "room" to fill the remaining space with "a"s when you're done. This is as if you're spending n value of k to initially fill each position with an "a". After that, each character will be considered by how much of an increase it is over "a", thus a "z" has a value of 25, because it's 25 "more" than an "a". That also coincidentally makes thing easier with a 0-indexed alphabet reference string.

Then start with as many "z"s as you can fit in k, and use any leftover k for the middle character. Then fill out the start of ans with "a"s.



https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/discuss/1038789/C%2B%2B-Python-Javascript-Easy-Solution-w-Explanation-or-beats-100-100
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
'''
from typing import List
import string

class S:

    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        alpha = '_bcdefghijklmnopqrstuvwxy_'
        ans = 'z' * (k // 25)
        if k % 25:
            ans = alpha[k % 25] + ans
        return 'a' * (n - len(ans)) + ans


n = 3
k = 27
print(S().getSmallestString(n, k))
