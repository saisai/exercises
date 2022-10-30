'''
https://leetcode.com/problems/rotate-list/
https://leetcode.com/problems/rotate-list/solutions/883101/python-3-on-explanation/

Explanation
Two pass
    first pass, get the length and tail node
    second pass, locate the new_head and disconnect it with it previous node
Connect tail node to original head node
Return new_head
Check comment for more detail

Implementation
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class S:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k: return head # special case
        tail = cur = head
        n = 0
        while cur and cur.next: # get size of linked list
            cur = cur.next
            n += 1
        tail = cur # get the tail
        n += 1                  # adjust the size
        k = k % n               # take mode of k in case k > n
        if not k: return head   # if k is zero, no rotation
        n = n - k - 1           # locate new haed node
        cur = head
        for _ in range(n): cur = cur.next
        new_head = cur.next     # get the new head
        cur.next = None         # delink all
        tail.next = head        # connect tail to original head
        return new_head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

r = S().rotateRight(head, 2)

while r:
    print(r.val)
    r = r.next
