
def flatten(itr):
    try:
        t = sum((flatten(e) for e in itr), list())
    except:
        t = [itr]
    return t
lst = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
print(flatten(lst))
