package org.rosettacode.learning.I;

import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static java.util.Arrays.stream;
public class IndexFiniteListsOfPositiveIntegers {
    static BigInteger rank(int[] x) {
        String s = stream(x).mapToObj(String::valueOf).collect(Collectors.joining("F"));
        return new BigInteger(s, 16);
    }

    static List<BigInteger> unrank(BigInteger n) {
        BigInteger sixteen = BigInteger.valueOf(16);
        String s = "";
        while(!n.equals(BigInteger.ZERO)) {
            s = "0123456789ABCDEF".charAt(n.mod(sixteen).intValue()) + s;
            n = n.divide(sixteen);
        }
        return stream(s.split("F")).map(x -> new BigInteger(x)).collect(Collectors.toList());
    }

    public static void main(String[] args) {
        int[] s = {1, 2, 3, 10, 100, 987654321};
        System.out.println(Arrays.toString(s));
        System.out.println(rank(s));
        System.out.println(unrank(rank(s)));
    }
}
