package com.mycompany.leetcode.TopInterview150.linkedlist.ReverseLinkedListIi;

import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;

public class ReverseLinkedListIi150ardyadipta {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head == null) return null;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        for(int i = 0; i < m - 1; i ++) pre = pre.next;

        ListNode start = pre.next;
        ListNode then = start.next;

        for(int i = 0; i < n - m;i++) {
            start.next = then.next;
            then.next = pre.next;
            pre.next = then;
            then = start.next;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        ReverseLinkedListIi150ardyadipta obj = new ReverseLinkedListIi150ardyadipta();
        ListNode result = obj.reverseBetween(head, 2, 4);
        while(result != null) {
            System.out.printf(result.val + " ");
            result = result.next;
        }

    }
}
