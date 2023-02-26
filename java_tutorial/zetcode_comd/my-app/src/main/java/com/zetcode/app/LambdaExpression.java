package com.zetcode.app;

import java.util.Arrays;

public class LambdaExpression {

    public static void main(String[] args) {
        String[] words = {"kind", "massive", "atom", "car", "blue"};

        Arrays.sort(words, (String s1, String s2) -> (s1.compareTo(s2)));

        System.out.println(Arrays.toString(words));
    }
}
