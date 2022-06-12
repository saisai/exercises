
cols = ['r', 'g', 'b']
S = ['-' for i in range(4)]

print(S)

def col(n, i):
    if n == i:
        print(S)
    elif i == 0:
        for j in range(3):
            S[i] = cols[j]
            col(n, i + 1)
    else:
        for j in range(3):
            if S[i-1] != cols[j]:
                S[i] = cols[j]
                col(n, i + 1)

col(4, 0)

