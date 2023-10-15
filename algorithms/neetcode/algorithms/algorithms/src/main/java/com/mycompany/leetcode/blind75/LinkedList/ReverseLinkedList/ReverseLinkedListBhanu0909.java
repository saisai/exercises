package com.mycompany.leetcode.blind75.LinkedList.ReverseLinkedList;

import com.mycompany.goodrich6thedition.ch07.List;
import com.mycompany.leetcode.blind75.LinkedList.ListNode;

public class ReverseLinkedListBhanu0909 {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode  current = head;

        while(current != null) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4, new ListNode(5));

//        while(head != null) {
//            ListNode next = head.next;
//            System.out.println(next.val);
//            head = next.next;
//        }
        ReverseLinkedListBhanu0909 obj = new ReverseLinkedListBhanu0909();
        ListNode result = obj.reverseList(head);

        while(result != null) {
            System.out.print(result.val + " ");
            ListNode tmp = result.next;
            result = tmp;
        }
    }
}
