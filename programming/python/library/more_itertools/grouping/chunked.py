from more_itertools import chunked

print(*chunked([1,2,3,4,5,6,7], 3))
print(list(chunked([1,2,3,4,5,6,7], 3)))

for data in chunked([1,2,3,4,5,6,7], 3):
    print(data)
