package com.mycompany.leetcode.TopInterview150.linkedlist.AddTwoNumbers;

import com.mycompany.goodrich6thedition.ch07.List;
import com.mycompany.leetcode.TopInterview150.linkedlist.ListNode;

public class AddTwoNumbers150rahulvarma5297 {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode dummyHead = new ListNode(0);
        ListNode tail = dummyHead;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int digit1 = (l1 != null) ? l1.val : 0;
            int digit2 = (l2 != null) ? l2.val : 0;

            int sum = digit1 + digit2 + carry;
            int digit = sum % 10;
            carry = sum / 10;

            tail.next = new ListNode(digit);
            tail = tail.next;

            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;

        }

        ListNode result = dummyHead.next;
        dummyHead.next = null;
        return result;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

        AddTwoNumbers150rahulvarma5297 obj = new AddTwoNumbers150rahulvarma5297();
        ListNode result = obj.addTwoNumbers(l1, l2);

        while(result != null) {
            System.out.println(result.val);
            result = result.next;
        }

    }
}
