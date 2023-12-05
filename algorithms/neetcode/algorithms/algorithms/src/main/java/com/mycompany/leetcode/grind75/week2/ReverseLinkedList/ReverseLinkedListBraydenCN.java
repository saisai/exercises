package com.mycompany.leetcode.grind75.week2.ReverseLinkedList;

import com.mycompany.leetcode.grind75.week1.ListNode;

public class ReverseLinkedListBraydenCN {
    public ListNode reverseList(ListNode head) {
        /* iterative solution */
        ListNode newHead = null;
        while(head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }

    public ListNode reverseListRecursive(ListNode head) {
        /* recursive solution */
        return reverseListInt(head, null);
    }

    private ListNode reverseListInt(ListNode head, ListNode newHead) {
        if (head == null)
            return newHead;
        ListNode next = head.next;
        head.next = newHead;
        return reverseListInt(next, head);
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        ReverseLinkedListBraydenCN obj = new ReverseLinkedListBraydenCN();
        ListNode results = obj.reverseList(head);
        while(results != null) {
            System.out.print(results.val + " ");
            ListNode tmp = results.next;
            results = tmp;
        }
    }
}
