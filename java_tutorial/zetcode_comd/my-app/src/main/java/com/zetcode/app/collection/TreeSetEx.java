package com.zetcode.app.collection;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

public class TreeSetEx {
    public static void main(String[] args) {

        List<String> brands = new ArrayList<>();

        brands.add("Pepsi");
        brands.add("Amazon");
        brands.add("Volvo");
        brands.add("IBM");
        brands.add("HP");
        brands.add("Apple");
        brands.add("Starbucks");

        TreeSet<String> brands2 = new TreeSet<>();
        brands2.addAll(brands);

        System.out.println(brands2);
        System.out.println(brands2.descendingSet());

        System.out.println(brands2.first());
        System.out.println(brands2.last());

        System.out.println(brands2.headSet("IBM", true));
        System.out.println(brands2.tailSet("IBM", false));
        System.out.println(brands2.subSet("Apple", true, "Starbucks", true));
    }
}
