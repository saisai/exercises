package com.zetcode.app.collection;

import java.util.ArrayList;
import java.util.List;

class Base {}

public class ArrayListMultipleEx {

    public static void main(String[] args) {
        List da = new ArrayList();

        da.add("Java");
        da.add(3.5);
        da.add(55);
        da.add(new Base());

        for(Object el: da) {
            System.out.println(el);
        }

    }
}
