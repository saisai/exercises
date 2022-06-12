
cols = ['b1', 'b2', 'g']
size = len(cols)
print(size)
S = ['-' for i in range(size)]


new_S = []

inner_size = size
print(S)

def col(n, i):
    if n == i:
        if S != [['b1', 'g', 'b2'], ['b2', 'g', 'b1']]:
            new_S.append(S)
    elif i == 0:
        for j in range(inner_size):
            S[i] = cols[j]
            col(n, i + 1)
    else:
        for j in range(inner_size):
            if S[i-1] != cols[j]:
                S[i] = cols[j]
                col(n, i + 1)

col(size, 0)
#print(new_S)

for a in new_S:
    print(a)

