'''
https://leetcode.com/problems/swapping-nodes-in-a-linked-list
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1010898/python-3-two-pass-on-explanation

Explanation
    Find first_k (th) node and last_k (th) node & their previous node
    Then swap both & their previous node respectively
    Read comment in the code block for more detail
    Time complexity: O(N)
Implementation
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class S:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = cur = head
        prev1, first_k = dummy, head
        cnt = 0
        while cur:
            if cnt < k - 1:
                prev1 = first_k
                first_k = first_k.next
            cnt += 1
            cur = cur.next
        prev2, last_k = dummy, head
        for i in range(cnt - k):
            prev2 = last_k
            last_k = last_k.next
        prev1.next, prev2.next = last_k, first_k
        last_k.next, first_k.next = first_k.next, last_k.next # swap first_k & last_k
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

r = S().swapNodes(head, 2)

while r:
    print(r.val)
    r = r.next

