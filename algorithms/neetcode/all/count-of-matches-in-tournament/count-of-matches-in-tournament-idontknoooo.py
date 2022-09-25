'''
https://leetcode.com/problems/count-of-matches-in-tournament/
https://leetcode.com/problems/count-of-matches-in-tournament/discuss/970375/python-3-math-olgn-explanation

Explanation
    Each round will have (n+1) // 2 team advance
    Next round will have n // 2 matches
    Time complexity: O(lgN), Space: O(1)
Implementation
'''

class S:

    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n != 1:
            ans += (n+1) // 2
            n //=2
        return ans

print(S().numberOfMatches(7))
