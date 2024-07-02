package org.example.digitaloceancom.javaLinkedList;

import java.util.Deque;
import java.util.LinkedList;

public class LinkedListDequeOperationsDemo {
    public static void main(String[] args) {
        Deque names = new LinkedList();
        names.add(2);
        names.addFirst(1);
        names.addLast(3);
        names.addFirst(0);
        names.addLast(4);

        System.out.println("LinkedList content: " + names);
        System.out.println("LinkedList size: " + names.size());
        names.removeFirst();
        names.removeLast();

        System.out.println("LinkedList content: " + names);
        System.out.println("LinkedList size: " + names.size());
    }
}
