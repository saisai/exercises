'''
https://leetcode.com/problems/copy-list-with-random-pointer/
https://leetcode.com/problems/copy-list-with-random-pointer/solutions/864305/python-3-two-methods-recursive-iterative-explanation/

Approach #2. Recursive
    Recursively create copy of each node and connect their random nodes
    Time: O(n); Space: O(n)
'''
from random import random

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class S:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = dict()
        def deep_copy(node):
            if not node: return
            if node in d: return d[node]
            d[node] = n = Node(node.val)
            n.next = deep_copy(node.next)
            n.random = deep_copy(node.random)
            return n

        return deep_copy(head)

head = Node(7)
head.next = Node(13, 0)
head.next.next = Node(11, 4)
head.next.next.next = Node(10, 2)
head.next.next.next.next = Node(1, 0)

result = S().copyRandomList(head)
print(result)

print(head)
while result:
    print(result.val)
    result = result.next


