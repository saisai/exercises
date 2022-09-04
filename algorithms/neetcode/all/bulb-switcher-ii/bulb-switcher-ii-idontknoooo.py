'''
https://leetcode.com/problems/bulb-switcher-ii/
https://leetcode.com/problems/bulb-switcher-ii/discuss/1535818/python-3-math-o1

There are total 8 different status maximum
Give some test case and play around, you will find the pattern for smaller inputs

'''

class S:
    def flipLights(self, n: int, presses: int) -> int:
        if not presses:
            return 1
        elif n < 3:
            if n == 1:
                return 2
            elif presses >= 2:
                return 4
            else:
                return 3
        else:
            if presses >= 3:
                return 8
            elif presses == 2:
                return 7
            else:
                return 4

n = 1
presses = 1
print(S().flipLights(n, presses))
