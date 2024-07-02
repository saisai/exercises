package com.mycompany.leetcode.TopInterview150.linkedlist.LinkedListCycle;

import com.mycompany.goodrich6thedition.ch07.List;
import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;

public class LinkedListCycle150fabrizio3 {
    public boolean hasCycle(ListNode head) {
        if(head == null) return false;
        ListNode walker = head;
        ListNode runner = head;
        while(runner.next != null && runner.next.next != null) {
            walker = walker.next;
            runner = runner.next.next;
            if(walker == runner) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(3);
        head.next = new ListNode(2);
        head.next.next = new ListNode(0);
        head.next.next.next = new ListNode(-4);

        LinkedListCycle150fabrizio3 obj = new LinkedListCycle150fabrizio3();
        obj.hasCycle(head);
    }
}
