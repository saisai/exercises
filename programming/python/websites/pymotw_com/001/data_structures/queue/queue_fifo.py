
import queue

q = queue.Queue()

for i in range(10):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
