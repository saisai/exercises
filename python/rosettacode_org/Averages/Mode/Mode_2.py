from collections import Counter
def modes(values):
    count = Counter(values)
    best = max(count.values())
    return [k for k,v in count.items() if v == best]

print(modes([1,3,6,6,6,6,7,7,12,12,17]))
print(modes((1,1,2,4,4)))
