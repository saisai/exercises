
import queue
pq = queue.PriorityQueue()
for item in ((3, "Clear drains"), (4, "Feed cat"), (5, "Make tea"), (1, "Solve RC tasks"), (2, "Tax return")):
    pq.put(item)

while not pq.empty():
    print(pq.get())
    #print(pq.get_nowait())

print("\nheapq\n")
from heapq import heappush, heappop, heapify
items = [(3, "Clear drains"), (4, "Feed cat"), (5, "Make tea"), (1, "Solve RC tasks"), (2, "Tax return")]
heapify(items)
while items:
    print(heappop(items))

