
L = [[4, 5, 6, [7, 8, 9]],1, 2, 3]

for ll in L:
    print(ll)
    if isinstance(ll, list):
        for number in ll:
            print(number, end=' ')
    else:
        print(ll, end=' ')
