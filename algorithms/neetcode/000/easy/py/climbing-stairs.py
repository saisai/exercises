
class S:

    @classmethod
    def climbStairs(cls, n):
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

print(S.climbStairs(2))

