from functools import lru_cache
@lru_cache(maxsize=1024)
def ids(n):
    if n in {1, 89}: return n
    else: return ids(sum(int(d) **2 for d in str(n)))

ids(15)
t = [ids(x) for x in range(1, 21)]
print(t)
tt = sum(ids(x) == 89 for x in range(1, 100000000))
print(tt)