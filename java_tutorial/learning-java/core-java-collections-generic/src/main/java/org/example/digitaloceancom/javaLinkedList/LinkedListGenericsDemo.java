package org.example.digitaloceancom.javaLinkedList;

import java.util.LinkedList;
import java.util.List;

public class LinkedListGenericsDemo {
    public static void main(String[] args)
    {
        List<String> names = new LinkedList<>();
        names.add("Rams");
        names.add("Posa");
        names.add("Chinni");
        // We cannot add other than Strings
//         names.add(2011);

        System.out.println("LinkedList content: " + names);
        System.out.println("LinkedList size: " + names.size());
    }
}
