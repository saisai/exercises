import math

print(dir(math))
print()

def lcm(a, b): return abs(a * b) / math.gcd(a, b) if a and b else 0

print(lcm(12, 18))
print(lcm(-6, 14))

assert lcm(0,2) == lcm(2, 0) == 0
