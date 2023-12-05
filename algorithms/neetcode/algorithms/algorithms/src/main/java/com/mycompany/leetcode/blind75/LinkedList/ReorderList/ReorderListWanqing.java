package com.mycompany.leetcode.blind75.LinkedList.ReorderList;

import com.mycompany.leetcode.blind75.LinkedList.ListNode;

public class ReorderListWanqing {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null) return;

        // find the middle of the list
        ListNode p1 = head;
        ListNode p2 = head;
        while(p2.next != null && p2.next.next != null) {
            p1 = p1.next;
            p2 = p2.next.next;
        }

        //Reverse the half after middle  1->2->3->4->5->6 to 1->2->3->6->5->4
        ListNode preMiddle = p1;
        ListNode preCurrent = p1.next;
        while(preCurrent.next != null) {
            ListNode current = preCurrent.next;
            preCurrent.next = current.next;
            current.next = preMiddle.next;
            preMiddle.next = current;
        }

        //Start reorder one by one  1->2->3->6->5->4 to 1->6->2->5->3->4
        p1 = head;
        p2 = preMiddle.next;
        while(p1 != preMiddle) {
            preMiddle.next = p2.next;
            p2.next = p1.next;
            p1.next = p2;
            p1 = p2.next;
            p2 = preMiddle.next;
        }
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));

        ReorderListWanqing obj = new ReorderListWanqing();
        obj.reorderList(head);

        while(head != null) {
            System.out.print(head.val + " ");
            ListNode tmp = head.next;
            head = tmp;
        }
    }
}
