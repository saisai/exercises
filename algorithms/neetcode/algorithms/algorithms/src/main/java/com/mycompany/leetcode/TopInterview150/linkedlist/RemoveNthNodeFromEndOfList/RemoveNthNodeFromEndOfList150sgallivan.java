package com.mycompany.leetcode.TopInterview150.linkedlist.RemoveNthNodeFromEndOfList;

import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;

public class RemoveNthNodeFromEndOfList150sgallivan {
    public ListNode removeNthFromEnd(ListNode head ,int n) {
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
        RemoveNthNodeFromEndOfList150sgallivan obj = new RemoveNthNodeFromEndOfList150sgallivan();
        ListNode result = obj.removeNthFromEnd(head, 2);
        while(result != null) {
            System.out.printf("%d ", result.val);
            result = result.next;
        }
    }
}
