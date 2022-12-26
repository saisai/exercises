import itertools
def harshad():
    for n in itertools.count(1):
        #print([int(ch) for ch in str(n)])
        if n % sum(int(ch) for ch in str(n)) == 0:
            yield n


print(list(itertools.islice(harshad(), 0, 20)))


for n in harshad():
    if n > 1000:
        print(n)
        break


from itertools import count, islice
harshad = (n for n in count(1) if n % sum(int(ch) for ch in str(n)) == 0)
print(list(islice(harshad, 0, 20)))

t = next(x for x in harshad if x > 1000)
print(t)

