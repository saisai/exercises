'''
https://leetcode.com/problems/fraction-addition-and-subtraction/
https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/1318891/python-3-math-simulation-gcd-explanation

Explanation
    Intuition: Simulation seems like a fine solution, with basic Math, it should be straight forward.
    Simulation the following process:
        Find each (numerator, divisor) in expression, calculate the product of all divisors and store at multiple
        Calculate new numerator which is the sum of numerator * multiple // divisor named as s, and new divisor is now becomes to multiple
        Find greatest common divisor (GCD), which is divisor, between new numerator (s) and new divisor (multiple)
        Divide both s and multiple by divisor and return the final faction

Implementation
'''

class S:

    def fractionAddition(self, expression: str) -> str:
        pairs, cur, sign, multiple = [], '', 0, 1
        for c in expression+'+':
            if not sign:
                if c == '-': sign = -1
                else: sign, cur = 1, cur + c
            elif c in '+':
                left, right = cur.split('/')
                pairs.append((abs(int(left)) * sign, abs(int(right))))
                multiple *= pairs[-1][1]
                sign, cur = -1 if c == '-' else 1, ''
            else: cur += c
        s = sum([n * multiple // d for n, d in pairs])
        def gcd(a,b ):
            while b: a, b = b, a % b
            return abs(a)
        divisor = gcd(s, multiple)
        return f'{s//divisor}/{multiple//divisor}'

expression = "-1/2+1/2"
print(S().fractionAddition(expression))

