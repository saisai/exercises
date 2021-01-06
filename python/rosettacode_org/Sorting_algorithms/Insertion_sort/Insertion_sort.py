
def insertion_sort(L):
    for i in range(1, len(L)):
        j = i - 1
        key = L[i]
        key = L[i]
        while (L[j] > key) and (j >= 0):
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key

L = [4, 65, 2, -31, 0, 99, 83, 782, 1]
insertion_sort(L)
print(L)
