'''
https://leetcode.com/problems/longest-ideal-subsequence/
https://leetcode.com/problems/longest-ideal-subsequence/discuss/2409282/python3-dp

'''
class S:

    def longestIdealString(self, s: str, k: int) -> int:

        dp = [0]*26
        for ch in s:
            i = ord(ch)-97
            dp[i] = 1 + max(dp[max(0, i -k ) : i+k+1], default=0)
        return max(dp)

s = "acfgbd"
k = 2
print(S().longestIdealString(s, k))
