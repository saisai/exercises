package com.tutorial.N;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Function;

public class NestedFunction {
    static String makeList(String separator) {
        AtomicInteger counter = new AtomicInteger();

        Function<String, String> makeItem = item -> counter.getAndIncrement() + separator + item + "\n";
        return makeItem.apply("first") + makeItem.apply("second") + makeItem.apply("third");
    }

    public static void main(String[] args) {
        System.out.println(makeList(". "));
    }
}
