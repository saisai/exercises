
for i in range(13, 100, 2):
    print(i, ' => ', sorted(range(1, i+1), key=str))

t = list(range(1, 13))
print(t)
print(sorted(list(map(str, t)))  )
print(list(  map(int, sorted(list(map(str, t)))  )))