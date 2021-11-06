from collections import deque
from itertools import islice, count

def fusc():
    q = deque([1])
    yield 0
    yield 1

    while True:
        x = q.popleft()
        q.append(x)
        yield x

        x += q[0]
        q.append(x)
        yield x

def longest_func():
    sofar = 0
    for i, f in zip(count(), fusc()):
        if f >= sofar:
            yield (i, f)
            sofar = 10 * sofar or 10

print("First 61:")
print(list(islice(fusc(), 61)))

print('\nLength records:')
for i, f in islice(longest_func(), 6):
    print(f'fusc({i}) = {f}')

idx = 0
for i in fusc():
    print('a ', i)
    idx += 1
    if idx == 20:
        break
