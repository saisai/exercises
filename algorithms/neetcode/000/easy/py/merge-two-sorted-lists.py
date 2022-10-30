
class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    
'''
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

while ll:
    print(ll.val)
    ll = ll.next
'''        
        

class S:

    def __call__(self, l1, l2):

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next


b = ListNode(2)
c= ListNode(3)

l1 = ListNode(1)
l1.next = b
b.next = c

l2 = ListNode(1)
bb = ListNode(3)
cc = ListNode(4)
l2.next = bb
bb.next = cc

d = S()(l1, l2)


while d:
    print(d.val)
    d = d.next
    

'''
while l1:
    print(l1.val)
    l1 = l1.next
'''
