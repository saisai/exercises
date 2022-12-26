from functools import lru_cache
@lru_cache(maxsize=1024)
def _ids(nt):
    if nt in {('1',), ('8', '9')}: return nt
    else: return _ids(tuple(sorted(str(sum(int(d) ** 2 for d in nt)))))

def ids(n):
    return int(''.join(_ids(tuple(sorted(str(n))))))

print(ids(1), ids(15))
t = [ids(x) for x in range(1, 21)]
print(t)

#sum(ids(x) == 89 for x in range(1, 100000000))
sum(ids(x) == 89 for x in range(1, 10000000))

print(_ids.cache_info())