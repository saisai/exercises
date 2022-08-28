'''
https://leetcode.com/problems/climbing-stairs/
https://www.youtube.com/watch?v=Y0lT9Fck7qI&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=15&ab_channel=NeetCode
'''


class S:

    def climbStairs(self, n: int) -> int:

        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

n = 3
print(S().climbStairs(n))

