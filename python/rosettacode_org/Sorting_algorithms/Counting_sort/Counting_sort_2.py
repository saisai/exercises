
def countingSort(a, min, max):
    count = [0] * (max - min + 1)
    for x in a:
        cnt[x - min] += 1

    return [x for x, n in enumerate(cnt, start=min)
            for i in range(n)]
