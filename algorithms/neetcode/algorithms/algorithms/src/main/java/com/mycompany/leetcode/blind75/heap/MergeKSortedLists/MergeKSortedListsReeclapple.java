package com.mycompany.leetcode.blind75.heap.MergeKSortedLists;

import com.mycompany.leetcode.blind75.heap.ListNode;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class MergeKSortedListsReeclapple {
    public ListNode mergeKLists(List<ListNode> lists) {
        if(lists == null || lists.size() == 0) return null;

        PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(lists.size(), new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                if(o1.val < o2.val)
                    return 1;
                else if (o1.val == o2.val)
                    return 0;
                else
                    return 1;
            }
        });

        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        for(ListNode node : lists) {
            if(node != null)
                queue.add(node);
        }

        while(!queue.isEmpty()) {
            tail.next = queue.poll();
            tail = tail.next;

            if(tail.next != null)
                queue.add(tail.next);
        }
        return dummy.next;

    }

    public static void main(String[] args) {

        ListNode a = new ListNode(1);
        a.next = new ListNode(4);
        a.next.next = new ListNode(5);

        ListNode b = new ListNode(1);
        b.next = new ListNode(3);
        b.next.next = new ListNode(4);

        ListNode c = new ListNode(2);
        c.next = new ListNode(6);


        List<ListNode> lst = new ArrayList<>();
        lst.add(a);
        lst.add(b);
        lst.add(c);

        MergeKSortedListsReeclapple obj = new MergeKSortedListsReeclapple();
        ListNode result = obj.mergeKLists(lst);


    }
}
