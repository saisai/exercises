package com.mycompany.leetcode.blind75.binary.ReverseBits;

public class ReverseBitsAmadou {
    public int reverseBits(int n) {
        if(n == 0)return 0;

        int result = 0;
        for(int i = 0; i < 32; i++) {
            result <<= 1;
            if((n & 1) == 1) result++;
            n >>= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        ReverseBitsAmadou obj = new ReverseBitsAmadou();
        int n = 0b00000010100101000001111010011100;
        System.out.println(obj.reverseBits(n));
    }
}
