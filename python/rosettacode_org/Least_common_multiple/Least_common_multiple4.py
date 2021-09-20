def lcm(p, q):
    p, q = abs(p), abs(q)
    m = p * q
    if not m: return 0
    while True:
        p %= q
        if not p: return m // q
        q %= p
        if not q: return m // p

print(lcm(-6, 14))
