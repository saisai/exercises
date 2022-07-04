
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class S:
    #@staticmethod
    def reverseList(self, head):

        # recursive: T O(n), M O(n)

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

head = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
h5 = ListNode(5)

head.next = h2
h2.next = h3
h3.next = h4
h4.next = h5

#print(S.reverseList(head))
result = S().reverseList(head)

while result:
    print(result.val)
    result = result.next

