package com.tutorial.A;

import javax.swing.*;

public class AnonymousRecursion {

    public static long fib(int n) {
        if(n < 0)
            throw new IllegalArgumentException("n can not be a negative number");

        new Object() {
            void hello() {
                System.out.print("hello world");
            }
        }.hello();

        return new Object() {
            private long fibInner(int n) {
                return (n < 2 ) ? n : (fibInner(n - 1) + (fibInner(n - 2)));
            }

        }.fibInner(n);
    }

    public static void main(String... args) {

        long result = fib(10);
        System.out.print(result);

    }
}
