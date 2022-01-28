# map(function, iterable, ...)


def hello(s, b):
    return str(b) + ' test ' + str(s)

p = map(hello, list(range(1, 10)), list(range(1, 10)))

print(p)
print(list(p))



def test(s):
    ll = []
    for i in range(0, s):
        ll.append(i)
    return ll

print(list(map(test, list(range(0, 10)))))

def test_dict(s):
    ll = {}
    dd = []
    for i in range(0, s):
        dd.append(i)
    if dd:
        return {s: dd}

print(list(map(test_dict, list(range(0, 10)))))


