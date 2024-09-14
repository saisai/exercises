

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class S:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head 

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

result = S().removeNthFromEnd(head, 2)

print(result)

while result:
    print(result.val)
    tmp = result.next
    result = tmp

