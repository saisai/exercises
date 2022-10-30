'''
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/1428517/python-3-hash-table-bitmask-tuple-on-two-implementations-explanation

Approach #1 Masking with Tuple
    There are 5 vowels, and we only care whether the substring contains even or odd number of same vowel. That being said:
        'aabc' is essentially same as 'aabcaa', because there are even numbers of a in both string
    Say 0 means even number of a vowel and 1 means odd numbers of a vowel, given 5 vowels, there are only 32 different permutations of a length 5 tuple with only 0 and 1 in it. We will call any of the permutation mask.
    Anyhow, we will run a prefix count on substring vowels, to calculate the result, we need to take the index of the current mask minus the lowest index of the same mask
'''

import sys

import collections

class S:
    def findTheLongestSubstring(self, s: str) -> int:
        d = collections.defaultdict(lambda: sys.maxsize)
        print(d,)
        cur = (0, 0, 0, 0, 0)   # current mask
        ans = d[cur] = -1       # initialize result
        #print(d, d[(0, 0, 0,)])
        vowel = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u':4} # index mapping
        for i, c in enumerate(s):
            if c in vowel:  # if `c` is a vowel, update the `cur` (mask)
                idx = vowel[c]
                cur = cur[:idx] + (1 - cur[idx], ) + cur[idx+1:]
            if d[cur] == sys.maxsize:
                d[cur] = i          # if mask is never recorded, recorded it since it's the lowest index of this current mask
                print('cur ', d[cur], d)
            ans = max(ans, i - d[cur]) # update `ans` by calculating `i - lower_idx_of_mask`
        return ans

s = "eleetminicoworoep"
print(S().findTheLongestSubstring(s))

