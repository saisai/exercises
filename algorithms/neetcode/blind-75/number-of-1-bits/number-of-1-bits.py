'''
https://www.youtube.com/watch?v=5Km3utixwZs&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=11&ab_channel=NeetCode
https://leetcode.com/problems/number-of-1-bits/

'''

def dec_to_bin(x):
    return int(bin(x)[2:])

class S:

    def hammingWeight(self, n: int) -> int:
        n = dec_to_bin(n)
        
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res


        print('n ', n)
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

n = '00000000000000000000000000001011'
n = int(n, 2)
print(n)
print(S().hammingWeight(n))
