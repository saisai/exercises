package com.mycompany.leetcode.blind75.LinkedList.RemoveNthNodeFromEndOfList;

import com.mycompany.leetcode.blind75.LinkedList.ListNode;

public class RemoveNthNodeFromEndOfListSgallivan {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fast = head, slow = head;
        for(int i = 0; i < n; i++) fast = fast.next;
        if(fast == null) return head.next;
        while(fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return head;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        RemoveNthNodeFromEndOfListSgallivan obj = new RemoveNthNodeFromEndOfListSgallivan();
        ListNode result = obj.removeNthFromEnd(head, 2);

        while(result != null) {
            System.out.print(result.val + " ");
            ListNode tmp = result.next;
            result = tmp;
        }
    }
}
