pn = 0
an = 0
dn = 0
tt = []
num = 20000
for n in range(1, num + 1):
    for x in range(1, n+1):
        n = int(n)
        if n%x == 0:
            tt.append(x)

    tt.pop(len(tt)-1)
    if sum(tt) == n:
        pn += 1
        tt = []
    elif sum(tt) > n:
        an += 1
        tt = []
    elif sum(tt) < n:
        dn += 1
        tt = []

print(str(pn) + " Perfect Numbers")
print(str(an) + " Abundant Numbers")
print(str(dn) + " Deficient Numbers")
