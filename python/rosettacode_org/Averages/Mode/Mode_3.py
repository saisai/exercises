
def onemode(values):
    return max(set(values), key=values.count)

print(onemode([1,3,6,6,6,6,7,7,12,12,17]))
print(onemode((1,1,2,4,4)))
