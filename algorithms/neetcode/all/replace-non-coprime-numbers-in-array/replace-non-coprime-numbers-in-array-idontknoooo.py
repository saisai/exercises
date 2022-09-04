'''
https://leetcode.com/problems/replace-non-coprime-numbers-in-array

https://leetcode.com/problems/replace-non-coprime-numbers-in-array/discuss/1824407/python-3-doubly-linked-list-explanation

Explanation
Pretty much brute force with help of Doubly Linked List
Use LinkedList since remove from list is slow O(N)
Btw, the stack solution is way better. Ignore this if you want a faster solution.
Implementation

'''
from math import gcd

from typing import List

class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class S:

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        prev = cur = root = ListNode(int(1e9+7))
        for num in nums:
            cur = ListNode(num)
            cur.prev = prev
            prev.next = cur
            prev = cur
        prev, cur = root.next, root.next.next
        while cur:
            tmp = gcd(cur.val, prev.val)
            if tmp > 1:
                lcm_node = ListNode(cur.val * prev.val // tmp)
                prev.prev.next = lcm_node
                lcm_node.prev = prev.prev
                lcm_node.next = cur.next
                if cur.next:
                    cur.next.prev = lcm_node
                cur.prev = cur.next = prev.prev = prev.next = None
                prev, cur = lcm_node.prev, lcm_node
            else:
                head, prev, cur = prev, cur, cur.next

        ans, root = [], root.next
        while root:
            ans.append(root.val)
            root = root.next
        return ans


nums = [6,4,3,2,7,6,2]
print(S().replaceNonCoprimes(nums))

