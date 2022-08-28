'''
https://leetcode.com/problems/count-numbers-with-unique-digits/

https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/1416500/python-3-math-dp-explanation

Explanation
    f(0) = 1
    f(1) = 9 + f(0) = 10
    f(2) = 9 * 9 + f(1) = 91
    f(3) = 9 * 9 * 8 + f(2) = 739
    ...
    You got the idea
Implementation
'''

class S:

    def countNumbersWithUniqueDigits(self, n: int) ->int:

        ans = [1]
        for k in range(1, n+1):
            base = available = 9
            for _ in range(k-1):
                base *= available
                available -= 1
            ans.append(base+ans[-1])
        return ans[-1]

n = 2
print(S().countNumbersWithUniqueDigits(n))
