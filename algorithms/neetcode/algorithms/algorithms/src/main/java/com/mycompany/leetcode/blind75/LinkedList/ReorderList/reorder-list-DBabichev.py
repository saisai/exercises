
class ListNode:
    def __init__(self, val, next=None):
        self.val = val 
        self.next =next

class S:
    def reorderList(self, head):
        # step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev 
            prev = curr 
            curr = nextt
        slow.next = None 
        
        # step 3: merge lists 
        head1, head2 = head, prev 
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2 
            head2 = nextt 
        

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))
print("head ", head)
S().reorderList(head)

print(head)
while head:
    print(head.val, end=" ")
    tmp = head.next 
    head = tmp
print("")
