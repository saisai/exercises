
def mfac2(n, m): return n if n <= (m + 1) else n * mfac2(n - m, n)

for m in range(1, 6): print("%2i: %r" % (m, [mfac2(n, m) for n in range(1, 11)]))
