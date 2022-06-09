'''
https://leetcode.com/problems/climbing-stairs/
https://www.youtube.com/watch?v=Y0lT9Fck7qI&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=2&ab_channel=NeetCode
'''

class S:

    def __call__(self, n):

        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one

        return one

print(S()(2))
print(S()(3))
