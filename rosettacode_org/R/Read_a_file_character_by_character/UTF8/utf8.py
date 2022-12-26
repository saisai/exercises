
def get_next_character(f):
    """Reads one character from the given textfile"""
    c = f.read(1)
    while c:
        yield c
        c = f.read(1)

word = {}
with open('utf8.py', encoding='utf-8') as f:
    for c in get_next_character(f):
        if c not in word:
            word[c] = 1
        else:
            word[c] += 1

        print(c, sep="", end="")


#print(word)
print('w' in word)
print(word.get('w'))
#for key, val in word.items():
#    print(key, val)
