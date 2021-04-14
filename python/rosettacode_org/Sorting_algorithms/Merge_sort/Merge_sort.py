from heapq import merge


def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


t = "22 51 31 59 58 45 11 2  16 56 38 42 2  10 23 41 42 25 45 28 42"
print(list((map(int, t.split()))))
# chage list string to int string
tlst = list((map(int, t.split())))

print(merge_sort(tlst))