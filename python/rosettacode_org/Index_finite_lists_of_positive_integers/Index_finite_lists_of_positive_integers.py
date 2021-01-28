
def rank(x): return int('a'.join(map(str, [1] + x)), 11)

def unrank(n):
    s = ''
    while n: s, n = "0123456789a"[n%11] + s, n // 11
    return map(int, s.split('a')[1:])

l = [1, 2, 3, 10, 100, 987654321]

print(l)
n = rank(l)
print(n)
l = unrank(n)
print(list(l))


def unrank1(n):
    return map(len, bin(n)[3:].split("0")) if n else []

def rank1(n):
    return int("1" + "0".join("1"*a for a in x), 2) if x else 0

for x in range(11):
    print(x, unrank1(x), rank1(list(unrank1(x)))

x = [1, 2, 3, 5, 8]
print(x, rank1(x), unrank1(rank1(x)))
