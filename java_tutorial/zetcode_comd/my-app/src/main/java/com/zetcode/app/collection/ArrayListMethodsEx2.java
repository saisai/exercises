package com.zetcode.app.collection;

import java.util.ArrayList;
import java.util.List;

public class ArrayListMethodsEx2 {

    public static void main(String[] args) {

        List<String> names = new ArrayList<>();

        names.add("Jane");
        names.add(0, "Thomas");
        names.add(1, "Robin");
        names.add("David");
        names.add("Becky");

        System.out.println(names);

        System.out.println(names.isEmpty());
        System.out.println(names.contains("Jane"));
        System.out.println(names.contains("Robert"));

        System.out.println(names.indexOf("Jane"));

        System.out.println(names.subList(1, 4));

        names.clear();
        System.out.println(names.isEmpty());
        System.out.println(names);

    }
}
