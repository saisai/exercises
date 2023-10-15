package com.mycompany.leetcode.blind75.LinkedList.MergeKSortedLists;

import com.mycompany.leetcode.blind75.LinkedList.ListNode;

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
        ListNode tail = dummy;

        for(ListNode node : lists){
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

    private void printList(List<ListNode> head) {
        for(ListNode r : head) {
            while(r != null) {
                System.out.print(r.val + " ");
                ListNode tmp = r.next;
                r = tmp;
            }
            System.out.println();
        }
    }

    private void printList(ListNode r) {
        while(r != null) {
            System.out.print(r.val + " ");
            ListNode tmp = r.next;
            r = tmp;
        }
        System.out.println();

    }

    public static void main(String[] args) {
        ListNode a = new ListNode(1, new ListNode(4, new ListNode(5)));
        ListNode b = new ListNode(1, new ListNode(3, new ListNode(4)));
        ListNode c = new ListNode(2, new ListNode(6));

        List<ListNode> lst = new ArrayList<>() {{
            add(a);
            add(b);
            add(c);
        }};

        MergeKSortedListsReeclapple obj = new MergeKSortedListsReeclapple();
        obj.printList(lst);
        ListNode results = obj.mergeKLists(lst);
        obj.printList(results);

    }
}
