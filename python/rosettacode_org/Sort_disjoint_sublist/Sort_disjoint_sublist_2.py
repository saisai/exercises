def sort_disjoint_sublist(data, indices):
    indices = sorted(indices)
    values = sorted(data[i] for i in indices)
    for index, value in zip(indices, values):
        print(index, value)
        data[index] = value

d = [7, 6, 5, 4, 3, 2, 1, 0]
i = set([6, 1, 7])

sort_disjoint_sublist(d, i)
print(d)

