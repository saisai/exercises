package com.mycompany.leetcode.grind75.week2.MiddleOfTheLinkedList;

import com.mycompany.leetcode.grind75.week1.ListNode;

public class MiddleOfTheLinkedListLee215 {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public static void main(String[] args) {
        ListNode root = new ListNode(1, new ListNode(2, new ListNode(3,
                new ListNode(4, new ListNode(5, new ListNode(6))))));
        MiddleOfTheLinkedListLee215 obj = new MiddleOfTheLinkedListLee215();
        ListNode result = obj.middleNode(root);

        while(result != null) {
            System.out.print(result.val + " ");
            ListNode tmp = result.next;
            result = tmp;
        }
    }
}
