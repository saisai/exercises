package com.tutorial.A;

import java.util.Arrays;
import java.util.Objects;

public class ArrayConcatenation {
    public static Object[] concat(Object[] arr1, Object[] arr2) {
        Object[] res = new Object[arr1.length + arr2.length];

        System.arraycopy(arr1, 0, res, 0, arr1.length);
        System.arraycopy(arr2, 0, res, arr1.length, arr2.length);

        return res;
    }

    public static void main(String... args) {
        Object[] a = {1, 2, 3};
        Object[] b = {4, 5, 6};

        Object[] result = concat(a, b);
        System.out.println(Arrays.toString(result));

        Object[] c = {"hello", "world"};
        Object[] d = {"Hi", "How are you?"};
        Object[] r = concat(c, d);

        for(Object e : r) {
            System.out.println(e);
        }

    }
}
