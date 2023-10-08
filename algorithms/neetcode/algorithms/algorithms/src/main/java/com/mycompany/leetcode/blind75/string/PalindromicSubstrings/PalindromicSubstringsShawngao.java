package com.mycompany.leetcode.blind75.string.PalindromicSubstrings;

public class PalindromicSubstringsShawngao {
    static int countSubstrings(String s) {
        int count = 0;
        if (s == null || s.length() == 0) return 0;

        for (int i = 0; i < s.length(); i++) { // i is the mid point
            count += extendPalindrome(s, i, i); // odd length;
            count += extendPalindrome(s, i, i + 1); // even length
        }

        return count;
    }

    static int extendPalindrome(String s, int left, int right) {
        int count = 0;
        while (left >=0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            count++; left--; right++;
        }
        return count;
    }

    public static void main(String[] args) {
        String s = "abc";
        System.out.println(countSubstrings(s));
    }
}
