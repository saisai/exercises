'''
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/discuss/1492366/python-3-greedy-explanation

Explanation
    When talking about swap, it's almost always a greedy operation, no easy way around
    There are only two scenarios, either 010101.... or 101010...., depends on the length of s, you might want to append an extra 0 or 1
    Simply count the mismatches and pick the less one, see more explanation in the code comment below
Implementation
'''

class S:

    def minSwaps(self, s: str) -> int:
        ans = n = len(s)
        zero, one = 0, 0
        for c in s:     # count number of 0 & 1s
            if c == '0':
                zero += 1
            else:
                one += 1
        if abs(zero - one) > 1: return -1 # not possible when cnt differ over 1
        if zero >= one: # '010101....'
            s1 = '01' * (n // 2) # when zero == one
            s1 += '0' if n % 2 else '' # when zero > one
            cnt = sum(c1 != c for c1, c in zip(s1, s))
            ans = cnt // 2
        if zero <= one: # '101010....'
            s2 = '10' * (n // 2) # when zero == one
            s1 += '1' if n % 2 else '' # when zero == one
            cnt = sum(c2 != c for c2, c in zip(s2, s))
            ans = min(ans, cnt // 2)
        return ans

s = "111000"

print(S().minSwaps(s))

