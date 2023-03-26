package com.tutorial.C.Closures;


import java.util.List;
import java.util.function.IntSupplier;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.toList;
public class ValueCapture2 {
    public static void main(String... args) {
        List<IntSupplier> closures = IntStream.rangeClosed(0, 10)
                .<IntSupplier>mapToObj(i -> () -> i * i)
                .collect(toList());
        IntSupplier closure = closures.get(3);
        System.out.println(closure.getAsInt());
    }
}
