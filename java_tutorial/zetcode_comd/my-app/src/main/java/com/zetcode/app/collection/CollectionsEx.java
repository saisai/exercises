package com.zetcode.app.collection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class CollectionsEx {
    public static void main(String[] args) {
        Integer[] nums = { 4, 3, 2, 4, 5, 6, 4, 2, 7, 8, 9, 0, 1 };

        List<Integer> ns = new ArrayList<>(Arrays.asList(nums));

        System.out.println("Default order:");
        System.out.println(ns);

        System.out.println("Ascending order:");
        Collections.sort(ns);
        System.out.println(ns);

        System.out.println("Descending order:");
        Collections.reverse(ns);
        System.out.println(ns);

        System.out.println("Swapping the first and the last elements:");
        Collections.swap(ns, 0, ns.size()-1);
        System.out.println(ns);

        System.out.println("Replacing all 4s with 0s:");
        Collections.replaceAll(ns, 4, 0);
        System.out.println(ns);

        System.out.println("Random order:");
        Collections.shuffle(ns);
        System.out.println(ns);

        System.out.println(Collections.max(ns));
        System.out.println(Collections.min(ns));


    }
}
