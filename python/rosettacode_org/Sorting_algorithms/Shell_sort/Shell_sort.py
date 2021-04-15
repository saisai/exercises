def shell(seq):
    print('shell ', id(seq))
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq[inc:], inc):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else inc * 5 // 11

data = [22, 7, 2, -5, 8, 4]
print(id(data))
shell(data)
print(id(data))
print(data)
print(id(data))