package com.tutorial.C.Continued_fraction.Arithmetic;

import java.util.*;

public class ConstructFromRationalNumber {

    final static class MyEntry<K, V> implements Map.Entry<K, V> {
        private final K key;
        private V value;

        public MyEntry(K key, V value) {
            this.key = key;
            this.value = value;
        }

        @Override
        public K getKey() {
            return key;
        }

        @Override
        public V getValue() {
            return value;
        }

        @Override
        public V setValue(V value) {
            V old = this.value;
            this.value = value;
            return old;
        }
    }
    private static class R2cf implements Iterator<Integer> {
        private int num;
        private int den;

        R2cf(int num, int den) {
            this.num = num;
            this.den = num;
        }

        @Override
        public boolean hasNext() {
            return den != 0;
        }

        @Override
        public Integer next() {
            int div = num / den;
            int rem = num % den;
            num = den;
            den = rem;
            return div;
        }
    }

    private static void iterate(R2cf generator) {
        generator.forEachRemaining(n -> System.out.printf("%d ", n));
        System.out.println();
    }

    public static void main(String[] args) {
        List<Map.Entry<Integer, Integer>> fracs = Arrays.asList(
                new MyEntry<Integer, Integer>(1, 123),
                new MyEntry<Integer, Integer>(3, 1),
                new MyEntry<Integer, Integer>(23, 8),
                new MyEntry<Integer, Integer>(13, 11),
                new MyEntry<Integer, Integer>(22, 7),
                new MyEntry<Integer, Integer>(-157, 77)
        );

        for (Map.Entry<Integer, Integer> frac : fracs) {
            System.out.printf("%4d / %-2d = ", frac.getKey(), frac.getValue());
            iterate(new R2cf(frac.getKey(), frac.getValue()));
        }

        System.out.println("\nSqrt(2) ->");
        List<Map.Entry<Integer, Integer>> root2 = Arrays.asList(
                new MyEntry<Integer, Integer>(    14_142,     10_000),
                new MyEntry<Integer, Integer>(   141_421,    100_000),
                new MyEntry<Integer, Integer>( 1_414_214,  1_000_000),
                new MyEntry<Integer, Integer>(14_142_136, 10_000_000)
        );

        for (Map.Entry<Integer, Integer> frac : root2) {
            System.out.printf("%8d / %-8d = ", frac.getKey(), frac.getValue());
            iterate(new R2cf(frac.getKey(), frac.getValue()));
        }

        System.out.println("\nPi ->");
        List<Map.Entry<Integer, Integer>> pi = Arrays.asList(
                new MyEntry<Integer, Integer>(         31,        10),
                new MyEntry<Integer, Integer>(        314,       100),
                new MyEntry<Integer, Integer>(      3_142,      1_000),
                new MyEntry<Integer, Integer>(     31_428,     10_000),
                new MyEntry<Integer, Integer>(    314_285,    100_000),
                new MyEntry<Integer, Integer>(  3_142_857,   1_000_000),
                new MyEntry<Integer, Integer>( 31_428_571,  10_000_000),
                new MyEntry<Integer, Integer>(314_285_714, 100_000_000)
        );

        for (Map.Entry<Integer, Integer> frac : pi) {
            System.out.printf("%9d / %-9d = ", frac.getKey(), frac.getValue());
            iterate(new R2cf(frac.getKey(), frac.getValue()));
        }

    }
}

// https://stackoverflow.com/questions/3110547/java-how-to-create-new-entry-key-value