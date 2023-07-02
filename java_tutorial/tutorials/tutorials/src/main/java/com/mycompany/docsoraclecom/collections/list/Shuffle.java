package com.mycompany.docsoraclecom.collections.list;

import java.util.*;

public class Shuffle {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        String[] testArgs = {"Hello", "How", "Test"};
        for(String a : testArgs) {
            list.add(a);
        }
        Collections.shuffle(list, new Random());
        System.out.println(list);
        System.out.println();
        shuffle2(testArgs);
    }

    static void shuffle2(String[] args) {
        List<String> list = Arrays.asList(args);
        Collections.shuffle(list);
        System.out.println(list);
    }
}
