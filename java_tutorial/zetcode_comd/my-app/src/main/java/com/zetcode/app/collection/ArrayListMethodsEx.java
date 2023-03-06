package com.zetcode.app.collection;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ArrayListMethodsEx {

    public static void main(String[] args) {
        List<String> names = new ArrayList<>();
        names.add("Jane");
        names.add("Thomas");
        names.add("Robin");
        names.add("David");
        names.add("Becky");

        System.out.println(names);
        names.set(1, "Tom");
        System.out.println(names);

        System.out.format("There are %d elements in the collection%n", names.size());

        names.remove(1);
        System.out.format("There are %d elements in the collection%n",
                names.size());

        System.out.println(names.get(3));

        System.out.println("************");

        Iterator<String> it = names.iterator();

        while(it.hasNext()) {
            System.out.println(it.next());
        }

    }
}
