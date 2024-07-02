package com.mycompany.leetcode.TopInterview150.linkedlist.MergeTwoSortedLists;

import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;

public class MergeTwoSortedLists150yangliguang {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        if(l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        MergeTwoSortedLists150yangliguang obj = new MergeTwoSortedLists150yangliguang();
        ListNode result = obj.mergeTwoLists(l1, l2);
        while(result != null) {
            System.out.print( result.val + " ");
            result = result.next;
        }
    }
}
