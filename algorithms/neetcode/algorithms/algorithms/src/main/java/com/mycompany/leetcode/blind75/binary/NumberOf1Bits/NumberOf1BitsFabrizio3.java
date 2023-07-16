package com.mycompany.leetcode.blind75.binary.NumberOf1Bits;

public class NumberOf1BitsFabrizio3 {
    public static int hammingWeight(int n) {
        int ones = 0;
        while(n!= 0) {
            ones = ones + (n & 1);
            n = n >>> 1;
        }
        return ones;
    }

    public static void main(String[] args) {
        int n = 00000000000000000000000000001011;
        System.out.println(hammingWeight(n));
    }
}
