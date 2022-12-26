people = [('joe', 120), ('foo', 31), ('bar', 51)]
print(sorted(people))


print(people)

from operator import itemgetter

t = sorted(people, key=itemgetter(1))
print(t)


d = sorted(people, key=lambda item: item[1])
print(d)

l = sorted(people, key=lambda item: item[0])
print(l)
