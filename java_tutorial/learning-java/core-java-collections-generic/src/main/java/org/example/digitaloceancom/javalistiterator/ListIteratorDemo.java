package org.example.digitaloceancom.javalistiterator;

import java.util.LinkedList;
import java.util.List;

import java.util.ListIterator;

public class ListIteratorDemo {
    public static void main(String[] args) {
        List<String> names = new LinkedList<>();
        names.add("Rams");
        names.add("Posa");
        names.add("Chinni");

        // getting listiterator
        ListIterator<String> namesIterator = names.listIterator();

        // traversing elements
        while(namesIterator.hasNext()) {
            System.out.println(namesIterator.next());
        }

        // enhanced for loop creates internal iterator here
        for(String name: names) {
            System.out.println(name);
        }
    }
}
