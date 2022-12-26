from numpy import base_repr


def sumDigits(num, base=10):
    return sum(int(x, base) for x in list(base_repr(num, base)))

print(sumDigits(1))
print(sumDigits(12345))
print(sumDigits(123045))
print(sumDigits(0xfe, 16))
print(sumDigits(0xf0e, 16))