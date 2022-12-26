
def popcount(n):
    return bin(n).count("1")

results = [popcount(3**i) for i in range(30)]
print(results)

evil, odious, i = [], [], 0
while len(evil) < 30 or len(odious) < 30:
    p = popcount(i)
    if p % 2: odious.append(i)
    else: evil.append(i)
    i += 1

print(evil[:30])
print(odious[:30])
