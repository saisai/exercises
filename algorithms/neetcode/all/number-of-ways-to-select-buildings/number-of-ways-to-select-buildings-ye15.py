'''

https://leetcode.com/problems/number-of-ways-to-select-buildings/discuss/2248166/python3-dp
https://leetcode.com/problems/number-of-ways-to-select-buildings/

'''
class S:

    def numberOfWays(self, s: str) -> int:

        ans = n0 = n1 = n01 = n10 = 0
        for ch in s:
            if ch == '0':
                ans += n01
                n10 += n1
                n0 += 1
            else:
                ans += n10
                n01 += n0
                n1 += 1
        return ans

s = "001101"
print(S().numberOfWays(s))
