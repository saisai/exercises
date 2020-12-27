
def genfizzbuzz(numberlist, wordlist, *args):
    nml = [[numberlist[i], wordlist[i]] for i in range(len(numberlist))]
    for z in range(*args):
        res = ""
        for j in nml:
            if z % j[0] == 0:
                res += j[1]
        print(res or z)

genfizzbuzz([3, 5, 7], ['Fizz', 'Buzz', 'Baxx'], 1, 21)
