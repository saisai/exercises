package com.tutorial.C;

import java.util.Arrays;

public class CompareAListOfStrings {

    static boolean allEqual(String[] strings) {
        String stringA = strings[0];
        for (String string : strings) {
            if (!string.equals(stringA))
                return false;
        }
        return true;
    }

    static boolean isAscending(String[] strings) {
        String previous = strings[0];
        int index = 0;
        for (String string : strings) {
            if (index++ == 0)
                continue;
            if (string.compareTo(previous) < 0)
                return false;
            previous = string;
        }
        return true;
    }
    public static void main(String[] args) {
        String[][] arr = {{"AA", "AA", "AA", "AA"}, {"AA", "ACB", "BB", "CC"}};
        for(String[] a : arr) {
            System.out.println(Arrays.toString(a));
            System.out.println(Arrays.stream(a).distinct().count() < 2);
            System.out.println(Arrays.equals(Arrays.stream(a).distinct().sorted().toArray(), a));
            System.out.println("Allequal " + allEqual(a));
            System.out.println("isAscending " + isAscending(a));
        }
    }
}
