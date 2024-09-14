from itertools import count
from more_itertools import ichunked

all_chunks = ichunked(count(), 4)

print(all_chunks)

c_1, c_2, c_3 = next(all_chunks), next(all_chunks), next(all_chunks)

print(c_1)
print(*c_1)
print(*c_2)

c1, c2 = [next(all_chunks) for _ in range(0, 2)]

print(list(c1))
print(*c2)

