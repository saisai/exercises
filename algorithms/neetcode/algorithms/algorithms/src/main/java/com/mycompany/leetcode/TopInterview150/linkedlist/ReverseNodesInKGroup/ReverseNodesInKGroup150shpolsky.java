package com.mycompany.leetcode.TopInterview150.linkedlist.ReverseNodesInKGroup;

import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;

public class ReverseNodesInKGroup150shpolsky {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int count = 0;
        while(curr != null && count != k) {
            curr = curr.next;
            count++;
        }

        if(count == k) {
            curr = reverseKGroup(curr, k);
            while(count-- > 0) {
                ListNode tmp = head.next;
                head.next = curr;
                curr = head;
                head = tmp;
            }
            head = curr;
        }
        return head;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        ReverseNodesInKGroup150shpolsky obj = new ReverseNodesInKGroup150shpolsky();
        ListNode result = obj.reverseKGroup(head, 2);
        while(result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}
