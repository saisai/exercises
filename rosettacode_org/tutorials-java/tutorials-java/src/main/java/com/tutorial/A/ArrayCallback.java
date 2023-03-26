package com.tutorial.A;

import java.util.Arrays;

public class ArrayCallback {
    public static void main(String... args) {
        int[] myIntArray = {1, 2, 3, 4, 5};

        int sum = Arrays.stream(myIntArray)
                .map(x -> {
                    int cube = x * x * x;
                    System.out.println(cube);
                    return cube;
                })
                .reduce(0, (left, right) -> left + right); // <-- could substitue .sum() for .reduce(...) here.
        System.out.println("Sum :" + sum);
        }
}
