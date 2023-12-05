package org.rosettacode.learning.E;

import java.math.BigInteger;

public class EvenOrOdd {


    // Bitwise and
    static boolean isEvenBitWise(int i) {
        return (i & 1) == 0;
    }
    // modulo
    static boolean isEvenModulo(int i) {
        return (i % 2) == 0;
    }

    // Arbitrary precision bitwise
    static boolean isEvenPrecision(BigInteger i) {
        return i.and(BigInteger.ONE).equals(BigInteger.ZERO);
    }

    static boolean isEven(BigInteger i){
        return !i.testBit(0);
    }

    static boolean isEvenPrecisionModulo (BigInteger i){
        return i.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO);
    }

    public static void main(String[] args) {
        System.out.println(isEven(BigInteger.valueOf(100)));
        System.out.println(isEven(BigInteger.valueOf(101)));
    }
}


