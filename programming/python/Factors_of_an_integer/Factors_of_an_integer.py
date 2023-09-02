def factors(n):
    return [i for i in range(1, n + 1) if not n % i]

print(factors(10))
print(factors(100))

def factors2(n):
    return [i for i in range(1, n//2 + 1) if not n%i] + [n]

print(factors2(10))
print(factors2(45))