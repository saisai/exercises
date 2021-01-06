def insertion_sort(L):
    for i, value in enumerate(L):
        for j in range(i-1, -1, -1):
            if L[j] > value:
                L[j+1] = L[j]
                L[j] = value

L = [4, 65, 2, -31, 0, 99, 83, 782, 1]
insertion_sort(L)
print(L)
