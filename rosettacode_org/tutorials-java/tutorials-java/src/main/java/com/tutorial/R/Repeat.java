package com.tutorial.R;

import java.util.function.Consumer;
import java.util.stream.IntStream;

public class Repeat {
    static void repeat(int n, Consumer<Integer> fun) {
        IntStream.range(0, n).forEach(i -> fun.accept(i + 1));
    }

    public static void main(String... args) {
        repeat(3, (x) -> System.out.println("Exmaple " + x));
    }
}
