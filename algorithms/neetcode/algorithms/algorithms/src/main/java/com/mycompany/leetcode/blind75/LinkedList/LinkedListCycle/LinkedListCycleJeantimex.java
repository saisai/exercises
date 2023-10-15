package com.mycompany.leetcode.blind75.LinkedList.LinkedListCycle;

import com.mycompany.leetcode.blind75.LinkedList.ListNode;

public class LinkedListCycleJeantimex {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if(slow == fast)
            {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(3);
        head.next = new ListNode(2);
        head.next.next = new ListNode(0, new ListNode( -4));

        LinkedListCycleJeantimex obj = new LinkedListCycleJeantimex();
        boolean result = obj.hasCycle(head);

        System.out.println(result);
    }
}
