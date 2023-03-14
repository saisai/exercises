package com.tutorial.One;

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class HundredDoorsStream {
    public static void main(String... args) {
        String openDoors = IntStream.rangeClosed(0, 100)
                .filter(i -> Math.pow((int) Math.sqrt(i), 2) == i)
                .mapToObj(Integer::toString)
                .collect(Collectors.joining(", "));
        System.out.printf("Open doors: %s%n", openDoors);
    }
}
