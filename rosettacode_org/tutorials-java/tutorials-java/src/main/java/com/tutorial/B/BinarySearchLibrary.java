package com.tutorial.B;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class BinarySearchLibrary {

    public static void main(String... args) {
        int[] haystack = {1, 5, 6, 7, 8, 11};
        int needle = 5;
        int index = Arrays.binarySearch(haystack, needle);
        System.out.println(index);

        List<Integer> haystackList = new ArrayList<>();
        haystackList.add(1);
        haystackList.add(5);
        haystackList.add(6);
        haystackList.add(7);
        haystackList.add(8);
        haystackList.add(11);
        int index2 = Collections.binarySearch(haystackList, needle);
        System.out.println(index2);

    }
}
