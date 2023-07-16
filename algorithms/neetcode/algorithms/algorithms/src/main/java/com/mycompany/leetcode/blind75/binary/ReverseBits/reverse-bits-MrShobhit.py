
class S:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res<<1) + (n & 1)
            n >>= 1
        return res

n = int('00000010100101000001111010011100', 2)
print(S().reverseBits(n))
