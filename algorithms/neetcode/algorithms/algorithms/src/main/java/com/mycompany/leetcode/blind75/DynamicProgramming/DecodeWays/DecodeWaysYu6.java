package com.mycompany.leetcode.blind75.DynamicProgramming.DecodeWays;

public class DecodeWaysYu6 {
    static int numDecodes(String s) {
        return s.length() == 0 ? 0 : numDecodings(0, s);
    }

    static int numDecodings(int p, String s) {
        int n=s.length();
        if(p == n) return 1;
        if(s.charAt(p)=='0') return 0;
        int res = numDecodings(p+1, s);
        if(p <n-1 && (s.charAt(p)== '1' || s.charAt(p)== '2' && s.charAt(p+1) <'7'))
            res += numDecodings(p+2, s);
        return res;
    }

    public static void main(String[] args) {
        String s = "226";
        System.out.print(numDecodes(s));
    }
}
