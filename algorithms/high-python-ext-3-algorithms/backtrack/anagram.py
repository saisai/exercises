def anagram(s1, s2):

    c1 = [0] * 26
    c2 = [0] * 26

    print(c1)
    print(c2)

    for c in s1:
        pos = ord(c)-ord('a')
        print('pos ', pos, ord(c), ord('a'))
        c1[pos] = c1[pos] + 1

    for c in s2:
        pos = ord(c) - ord('a')
        c2[pos] = c2[pos] + 1


    print(c1)
    print(c2)
    return c1 == c2
r1 = anagram('apple', 'pleap')
print(r1)

