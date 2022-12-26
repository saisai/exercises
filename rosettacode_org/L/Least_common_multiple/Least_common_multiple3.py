def lcm(*values):
    values = set([abs(int(v)) for v in values])
    if values and 0 not in values:
        n = n0 = max(values)
        values.remove(n)
        while any( n % m for m in values):
            n += n0
        return n
    return 0

print(lcm(-6,14))
print(lcm(12, 18, 22))
