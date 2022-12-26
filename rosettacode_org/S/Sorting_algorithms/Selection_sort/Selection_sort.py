
def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst

t = selection_sort([4, 65, 2, -31, 0, 99, 2, 83, 782, 1])
print(t)
