
def countJewels(s, j):
    return sum(x in j for x in s)

print(countJewels("aAAbbbb", "aA"))
print(countJewels("ZZ", "z"))


def countJewels2(stones, jewels):
    jewelset = set(jewels)
    return sum(1 for stone in stones if stone in jewelset )

print(countJewels2("aAAbbbb", "aA"))
print(countJewels2("ZZ", "z"))