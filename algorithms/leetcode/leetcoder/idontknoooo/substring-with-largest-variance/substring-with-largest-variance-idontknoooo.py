'''
Explanation
Time complexity: O((1+26)*26/2*800), there will be (1+26)*26/2 = 351 for loops, on average there will be a 10000/26*2 ~= 800 length on two pointers walk. In total we are looking at a scale of O(1e5), which is approximately O(N)
See below for more explanation
Implementation
https://leetcode.com/problems/substring-with-largest-variance/discuss/2042949/python-3-kadanes-algorithm-two-pointers-explanation
https://leetcode.com/problems/substring-with-largest-variance/
'''

import collections
import string
class S:

    def largestVariance(self, s):
        d = collections.defaultdict(list)

        for i, c in enumerate(s):   # for each letter, create a list of its indices
            d[c].append(i)

        print(d)
        ans = 0
        for x, chr1 in enumerate(string.ascii_lowercase): # character 1
            for chr2 in string.ascii_lowercase[x+1:]:    # character 2
                if chr1 == chr2 or chr1 not in d or chr2 not in d:
                    continue
                prefix = i = p1 = p2 = 0
                hi = hi_idx = lo = lo_idx = 0
                n1, n2 = len(d[chr1]), len(d[chr2])
                while p1 < n1 or p2 < n2:
                    if p1 < n1 and p2 < n2:
                        if d[chr1][p1] < d[chr2][p2]:
                            prefix, p1 = prefix + 1, p1 + 1
                        else:
                            prefix, p2 = prefix-1, p2 + 1
                    elif p1 < n1:
                        prefix, p1 = prefix+1, p1+1
                    else:
                        prefix, p2 = prefix-1, p2+1
                    if prefix > hi:
                        hi, hi_idx = prefix, i
                    if prefix < lo:
                        lo, lo_idx = prefix, i
                    ans = max(ans, min(prefix-lo, i-lo_idx-1))
                    ans = max(ans, min(hi-prefix, i-hi_idx-1))
                    i += 1
        return ans

s = "aababbb"
print(S().largestVariance(s))

