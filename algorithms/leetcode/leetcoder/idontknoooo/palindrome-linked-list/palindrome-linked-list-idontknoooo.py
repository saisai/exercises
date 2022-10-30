'''
https://leetcode.com/problems/palindrome-linked-list/

https://leetcode.com/problems/palindrome-linked-list/discuss/2466415/python-3-o1-space-explanation

Explanation
    Reverse the latter half of linked list then compare two half lists to see if they are the same

Implementation

'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class S:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        n = 0
        while node: # count length of linked list
            node = node.next
            n += 1
        half = n // 2

        node = head
        for _ in range(half - 1):   # find the middle point
            node = node.next
        else:
            nxt = node.next
            node.next = None
            node = nxt

        def reverse(node):      # reverse the latter half
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev, node = node, nxt
            return prev
        node = reverse(node)

        for _ in range(half):       # compare two `half` lists to decide if it's palindrome
            if head.val != node.val:
                return False
            head, node = head.next, node.next
        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

testroot = head
while testroot:
    print(testroot.val)
    testroot = testroot.next
print("head ", head)
print(S().isPalindrome(head))
