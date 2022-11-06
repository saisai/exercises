
class Solution:
    def climbStairs(self, n: int) -> int:        
        def climb(i):
            if i == 1:
                return 1
            if i == 2:
                return 2            
            return climb(i - 1) + climb(i-2)
        return climb(n)

    def climbStairsMemo(self, n: int) -> int:

        memo = {}
        memo[1] = 1
        memo[2] = 2
        def climb(n):
            if n in memo:       # if the recurssion already done before first take a look-up in the look-up table
                return memo[n]  # Store the recurssion function in the look-up table and reuturn the stored look-up table function
            else:
                memo[n] = climb(n-1) + climb(n - 2)
                return memo[n]
        return climb(n)

print(Solution().climbStairs(2))
print(Solution().climbStairsMemo(5))


# https://leetcode.com/problems/climbing-stairs/solutions/1531764/python-detail-explanation-3-solutions-easy-to-difficult-recursion-dictionary-dp/
