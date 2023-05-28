package com.mycompany.leetcode.easy.LexicographicallySmallestPalindrome;

public class LexicographicallySmallestPalindromeJudgementdey {
    static String makeSmallestPalindrome(String s) {
        char[] c = s.toCharArray();
        int i = 0, j = c.length - 1;

        while(i < j) {
            if(c[i] < c[j]) {
                c[j--] = c[i++];
            } else {
                c[i++] = c[j--];
            }
        }
        return new String(c);
    }

    public static void main(String[] args) {
        String s = "egcfe";
        System.out.println(makeSmallestPalindrome(s));
    }
}
