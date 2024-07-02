package org.example.digitaloceancom.javaLinkedList;

import java.util.LinkedList;
import java.util.List;

public class LinkedListDemo {
    public static void main(String[] args) {
        List names = new LinkedList();
        names.add("Rams");
        names.add("Posa");
        names.add("Chinni");
        names.add(2011);
        System.out.println("LinkedList contet: " + names);
        System.out.println("LinkedList size: " + names.size());
    }
}
