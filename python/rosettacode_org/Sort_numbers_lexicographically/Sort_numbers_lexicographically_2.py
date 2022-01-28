n=13

print(sorted(range(1, n+1), key=str))

nn = list(range(1, 14))
print(nn)

mm = list(map(str,nn))

print(mm)

mmm = sorted(mm)
print(mmm)

intt = list(map(int, mmm))
print(intt)

