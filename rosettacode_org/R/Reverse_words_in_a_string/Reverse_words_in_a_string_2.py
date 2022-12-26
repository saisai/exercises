
import queue

results = [f.strip('\n') for f in open('test.txt', encoding='utf-8')]

for f in results:
    print(' '.join(f.split()[::-1]))

