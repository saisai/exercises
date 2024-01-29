package com.mycompany.leetcode.grind75.week8.MergeKSortedLists;

import com.mycompany.leetcode.grind75.week1.ListNode;

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
                    return -1;
                else if (o1.val == o2.val)
                    return 0;
                else
                    return 1;
            }
        });

        ListNode dummy = new ListNode(0);
        ListNode tail=dummy;

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
        List<ListNode>  lists = new ArrayList<>() {{
            add(new ListNode(1, new ListNode(2, new ListNode(5))));
            add(new ListNode(1, new ListNode(3, new ListNode(4))));
            add(new ListNode(2, new ListNode(6)));
        }};

//        for(ListNode ll : lists) {
//            while(ll != null) {
//                ListNode tmp;
//                System.out.print(ll.val + " ");
//                tmp = ll.next;
//                ll = tmp;
//            }
//            System.out.println();
//        }

        MergeKSortedListsReeclapple obj = new MergeKSortedListsReeclapple();
        ListNode result = obj.mergeKLists(lists);

        while(result != null) {
            ListNode  tmp;
            System.out.print(result.val + " ");
            tmp = result.next;
            result = tmp;
        }

    }
}
