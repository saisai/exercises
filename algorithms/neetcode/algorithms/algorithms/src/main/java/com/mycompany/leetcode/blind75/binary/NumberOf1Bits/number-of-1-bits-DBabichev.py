
class S:
    def hammingWeight(self, n):
        ans = 0
        while n:
            n &= (n - 1)
            ans += 1
        return ans

n = 0b00000000000000000000000000001011
print(S().hammingWeight(n))
