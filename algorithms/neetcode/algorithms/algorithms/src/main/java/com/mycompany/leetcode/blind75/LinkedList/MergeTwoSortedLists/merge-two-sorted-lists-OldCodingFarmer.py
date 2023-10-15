
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next 

class S:

    def mergeTwoListsIteratively(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next 
        cur.next = l1 or l2
        return dummy.next

    def mergeTwoListsRecursively(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next =  self.mergeTwoListsRecursively(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursively(l1, l2.next)
            return l2 

    def mergeTwoListsInPlace(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1

        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next 
        cur.next = l1 or l2
        return dummy.next 


def show_lists(head):
    while head != None:
        print(head.val, end=' ')
        tmp = head.next
        head = tmp 
    print("")

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

#result = S().mergeTwoListsIteratively(l1, l2)
#show_lists(result)

#result2 = S().mergeTwoListsRecursively(l1, l2)
#show_lists(result2)

result3 = S().mergeTwoListsInPlace(l1, l2)
show_lists(result3)
