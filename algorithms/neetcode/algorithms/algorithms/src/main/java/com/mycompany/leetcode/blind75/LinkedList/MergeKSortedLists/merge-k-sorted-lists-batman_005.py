import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class S:
    def mergeKLists(self, lists):
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val 

        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(h, (i.val, i))

        while h:
            node = heapq.heappop(h)[1]
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))

        return head.next 

a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))

lists =[a, b, c]

result = S().mergeKLists(lists)

while result:
    print(result.val)
    tmp = result.next
    result = tmp

