package com.zetcode.app.collection;

import java.util.HashSet;
import java.util.Set;

public class HashSetEx {
    public static void main(String[] args) {

        Set<String> brands = new HashSet<>() ;

        brands.add("Pepsi");
        brands.add("Amazon");
        brands.add("Volvo");
        brands.add("IBM");
        brands.add("IBM");

        System.out.println(brands);

        System.out.println(brands.isEmpty());
        System.out.println(brands.contains("Volvo"));
        brands.remove("Volvo");
        System.out.println(brands.contains("Volvo"));

        brands.clear();
        System.out.println(brands);
    }
}
