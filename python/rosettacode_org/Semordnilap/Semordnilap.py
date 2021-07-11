with open('../unixdict.txt') as f:
    wordset = set(f.read().strip().split())

revlist = (''.join(word[::-1]) for word in wordset)
pairs = set((wrd, rev) for wrd, rev in zip(wordset, revlist)
        if wrd < rev and rev in wordset)
print(len(pairs))
print(sorted(pairs, key=lambda p: (len(p[0]), p))[-5:])
