'''
https://www.youtube.com/watch?v=UcoN6UjAI64&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=14&ab_channel=NeetCode
https://leetcode.com/problems/reverse-bits/
'''

class S:

    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):
            bit = (n >> i) & i
            res = res | (bit << (31 - i ))
        return res
n = '00000010100101000001111010011100'

print(S().reverseBits(int(n)))
