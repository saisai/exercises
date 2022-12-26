
# Here is a stack implemented as linked list - with the same list interface.



class Stack:
    def __init__(self):
        self._first = None

    def __bool__(self):
        return self._first is not None

    def append(self, value):
        self._first = (value, self._first)

    def pop(self):
        if self._first is None:
            raise IndexError("pop from empty stack")
        value, self._first = self._first
        return value

s = Stack()
print(bool(s))
if not s:
    print("empty")

s.pop()
