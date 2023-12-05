package com.mycompany.leetcode.grind75.week1.MergeTwoSortedLists;

import com.mycompany.leetcode.grind75.week1.ListNode;

public class MergeTwoSortedListsYangliguang {
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
        MergeTwoSortedListsYangliguang obj = new MergeTwoSortedListsYangliguang();
        ListNode list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

        ListNode result = obj.mergeTwoLists(list1, list2);

        while(result != null) {
            System.out.print(result.val + " ");
            ListNode tmp = result.next;
            result = tmp;
        }
    }
}
