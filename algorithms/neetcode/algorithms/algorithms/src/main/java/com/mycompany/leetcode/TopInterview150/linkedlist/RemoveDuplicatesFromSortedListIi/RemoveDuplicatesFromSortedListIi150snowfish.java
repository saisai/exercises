package com.mycompany.leetcode.TopInterview150.linkedlist.RemoveDuplicatesFromSortedListIi;

import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;
import com.mycompany.leetcode.TopInterview150.linkedlist.RemoveNthNodeFromEndOfList.RemoveNthNodeFromEndOfList150sgallivan;

public class RemoveDuplicatesFromSortedListIi150snowfish {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return null;
        ListNode FakeHead = new ListNode(0);
        FakeHead.next = head;
        ListNode pre = FakeHead;
        ListNode cur = head;
        while(cur != null) {
            while(cur.next != null && cur.val == cur.next.val) {
                cur = cur.next;
            }
            if(pre.next == cur) {
                pre = pre.next;
            } else {
                pre.next = cur.next;
            }
        }
        return FakeHead.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(3, new ListNode(4, new ListNode(4, new ListNode(5)))))));
        RemoveDuplicatesFromSortedListIi150snowfish obj = new RemoveDuplicatesFromSortedListIi150snowfish();
        ListNode result = obj.deleteDuplicates(head);
        while(result != null) {
            System.out.printf("%d ", result.val);
            result = result.next;
        }
    }
}
