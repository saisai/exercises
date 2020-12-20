"""
# https://leetcode.com/problems/powx-n/
# Implement pow(x, n).

# Recursively calculate (pow(x, n//2))^2 if n is even or with additional factor of x if n is odd.
# Time - O(log n)
# Space - O(log n)



Implement pow(x, n), which calculates x raised to the power n (i.e. xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

https://leetcode.com/problems/powx-n/


"""

class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        neg = n < 0
        pos_result = self.pos_pow(x, abs(n))
        return 1 / pos_result if neg else pos_result


    def pos_pow(self, x, n):
        if n == 0:
            return 1

        temp = self.pos_pow(x, n // 2)
        temp *= temp

        return temp if n % 2 == 0 else temp * x


if __name__ == '__main__':
    s = Solution()
    x = 2.10000
    n = 3
    print(s.myPow(x, n))

    x = 2.00000
    n = -2
    print(s.myPow(x, n))
