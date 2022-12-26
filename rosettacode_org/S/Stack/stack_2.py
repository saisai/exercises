
# If you need to expose your stack to the world, you may want to create a simpler wrapper:


from collections import deque

class Stack:

    def __init__(self):
        self._items = deque()

    def append(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __bool__(self):
        return bool(self._items)


s = Stack()
print(bool(s))
s.append(1)
print(s)
