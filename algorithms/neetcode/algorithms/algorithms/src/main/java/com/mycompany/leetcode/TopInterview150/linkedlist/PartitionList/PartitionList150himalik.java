package com.mycompany.leetcode.TopInterview150.linkedlist.PartitionList;

import com.mycompany.goodrich6thedition.ch07.List;
import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;

public class PartitionList150himalik {
    public ListNode partition(ListNode head, int x) {
        ListNode left = new ListNode(0);
        ListNode right = new ListNode(0);

        ListNode leftTail = left;
        ListNode rightTail = right;

        while(head != null) {
            if(head.val < x) {
                leftTail.next = head;
                leftTail = leftTail.next;
            } else {
                rightTail.next = head;
                rightTail = rightTail.next;
            }
            head = head.next;
        }
        leftTail.next = right.next;
        rightTail.next = null;

        return left.next;
    }

    public static void main(String[] args) {
        PartitionList150himalik obj = new PartitionList150himalik();
        ListNode head = new ListNode(1, new ListNode(4, new ListNode(3, new ListNode(2, new ListNode(5, new ListNode(2))))));
        ListNode result = obj.partition(head, 3);
        while(result != null) {
            System.out.printf("%d ", result.val);
            result = result.next;
        }
    }

}
