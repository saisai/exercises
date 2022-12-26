
from collections import deque

value = [1, 2, 3, 4]
stack = deque(value)

stack.append(5)
print(len(stack))

print(stack.pop())
print(not stack)
