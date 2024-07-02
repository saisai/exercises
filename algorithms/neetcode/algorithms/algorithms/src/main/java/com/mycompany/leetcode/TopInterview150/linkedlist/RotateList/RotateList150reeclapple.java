package com.mycompany.leetcode.TopInterview150.linkedlist.RotateList;

import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;

public class RotateList150reeclapple {
    public ListNode rotateRight(ListNode head, int n) {
        if(head == null || head.next == null) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode fast = dummy, slow=dummy;

        int i;
        for(i = 0; fast.next != null; i++) // get the total length
            fast = fast.next;
        for(int j = i-n % i; j > 0; j--) // get the i-n%i th node
            slow = slow.next;

        fast.next = dummy.next;
        dummy.next = slow.next;
        slow.next = null;

        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        RotateList150reeclapple obj = new RotateList150reeclapple();
        ListNode result = obj.rotateRight(head, 2);

        while(result != null) {
            System.out.printf("%d ", result.val);
            result = result.next;
        }

    }
}
