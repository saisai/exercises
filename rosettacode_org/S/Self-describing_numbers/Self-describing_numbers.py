
def isSelfDescribing(n):
    s = str(n)
    return all(s.count(str(i)) == int(ch) for i, ch in enumerate(s))

t = [x for x in range(4000000) if isSelfDescribing(x)]
print(t)

t = [(x, isSelfDescribing(x)) for x in (1210, 2020, 21200, 3211000, 42101000, 521001000, 6210001000)]
print(t)
