def prime(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a**0.5) + 1)))

for i in range(1, 10):
    print(i, prime(i))

def prime2(a):
    if a == 2: return True
    if a < 2 or a % 2 == 0: return False
    return not any(a % x == 0 for x in range(3, int(a**0.55) + 1, 2))

for i in range(1, 10):
    print(i, prime2(i))

def prime3(a):
    if a < 2: return False
    if a == 2 or a == 3: return True # manually test 2 and
    if a % 2 == 0 or a % 3 == 0: return False # exclude multiples of 2 and 3

    maxDivisor = a**0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if a % d == 0: return False
        d += i
        i = 6 - i # this modifies 2 into 4 and viceversa

    return True

for i in range(1, 10):
    print(i, prime3(i))


import re
def isPrime(n):
    return not re.match(r'^1?$|^(11+?)\1+$', '1' * n)

t = [i for i in range(40) if isPrime(i)]
print(t)
