package com.mycompany.leetcode.blind75.binary.SumOfTwoIntegers;

public class SumOfTwoIntegersZhaolz {
    public int getSum(int a, int b) {
        if(a == 0) return b;
        if(b == 0) return a;
        while(b != 0) {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }

    public int getSubtract(int a, int b) {
        while(b != 0) {
            int borrow = (~a) & b;
            a = a ^ b;
            b = borrow << 1;
        }
        return a;
    }

    public int getSumRecursive(int a, int b) {
        return (b == 0) ? a : getSum(a ^ b, (a & b) << 1);
    }

    public int getSubtractRecursive(int a, int b) {
        return (b == 0) ? a : getSubtract(a ^ b, (~a & b) << 1);
    }

    // Get negative number
    public int negate(int x) {
        return ~x + 1;
    }

    public static void main(String[] args) {
        int a = 1, b = 2;
        SumOfTwoIntegersZhaolz obj = new SumOfTwoIntegersZhaolz();
        System.out.println(obj.getSum(a, b));
        System.out.println(obj.getSumRecursive(a, b));
    }
}
