
'''
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/discuss/2244004/python3-1-line

'''

class S:

    def minBitFlips(self, start: int, goal: int) -> int:

        return bin(start^goal).count('1')

start = 10
goal = 7
print(S().minBitFlips(start,goal))
