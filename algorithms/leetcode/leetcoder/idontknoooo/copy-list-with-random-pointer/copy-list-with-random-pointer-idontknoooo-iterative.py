'''
https://leetcode.com/problems/copy-list-with-random-pointer/
https://leetcode.com/problems/copy-list-with-random-pointer/solutions/864305/python-3-two-methods-recursive-iterative-explanation/
Approach #1. Iterative
Use hash table to store information {original_node: new_node}
Two pass
    First create new node and connect with next
    Second use hash table to connect random node
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
        d = {None: None}
        dummy = Node(-1)
        cur, new_cur = head, dummy
        while cur:
            new_cur.next = d[cur] = Node(cur.val)
            cur, new_cur = cur.next, new_cur.next
        cur, new_cur = head, dummy.next
        while cur:
            new_cur.random = d[cur.random]
            cur, next_cur = cur.next, new_cur.next
        return dummy.next

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


