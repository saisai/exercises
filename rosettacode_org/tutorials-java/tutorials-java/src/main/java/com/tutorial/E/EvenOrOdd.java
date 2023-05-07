package com.tutorial.E;

import java.math.BigInteger;

public class EvenOrOdd {

    public static boolean isEvenBitwise(int i) {
        return (i & 1) == 0;
    }

    public static boolean isEvenModulo(int i) {
        return (i % 2) == 0;
    }

    public static boolean isEvenPrecisionBitwise(BigInteger i) {
        return i.and(BigInteger.ONE).equals(BigInteger.ZERO);
    }

    public static boolean isEvenPrecisionBitTest(BigInteger i) {
        return !i.testBit(0);
    }

    public static boolean isEvenPrecisionModulo(BigInteger i) {
        return i.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO);
    }

    public static void main(String[] args) {
        for(int i= 1; i < 10; i++) {
            System.out.printf("%d  %s%n", i, isEvenModulo(i));
            System.out.printf("%d  %s%n", i, isEvenBitwise(i));
            System.out.printf("%d  %s%n", i, isEvenPrecisionBitwise(BigInteger.valueOf(i)));
        }
    }

}
