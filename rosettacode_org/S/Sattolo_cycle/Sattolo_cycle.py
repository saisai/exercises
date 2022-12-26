from random import randrange

def sattoloCycle(items):
    for i in range(len(items) - 1, 0, -1):
        j = randrange(i) # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]

for _ in range(10):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sattoloCycle(lst)
    print(lst)
