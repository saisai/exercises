package com.tutorial.C.Closures;

import java.util.ArrayList;
import java.util.function.Supplier;

public class ValueCapture {
    public static void main(String... args) {
        ArrayList<Supplier<Integer>> funcs = new ArrayList<>();
        for(int i = 0; i < 10; i++) {
            int j = i;
            funcs.add(() -> j * j);
        }

        Supplier<Integer> foo = funcs.get(3);
        System.out.println(foo.get());
    }
}
