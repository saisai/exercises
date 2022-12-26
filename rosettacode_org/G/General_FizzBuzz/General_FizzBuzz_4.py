
from collections import defaultdict

n = 100
mods = {
    3: "Fizz",
    5: "Buzz",
}

def fizzbuzz(n=n, mods=mods):
    factors = defaultdict(list)
    for mod in mods:
        factors[mod].append(mod)

    for i in range(1, n+ 1):
        res = ""
        for mod in sorted(factors.pop(i)):
            factors[i+mod].append(mod)
            res += mods[mod]
        yield res or str(i)

if __name__ == '__main__':
    n = int(input())
    mods = { int(k): v for k,v in (input().split(maxsplit=1) for _ in range(3)) }
    for line in fizzbuzz(n, mods):
        print(line)
