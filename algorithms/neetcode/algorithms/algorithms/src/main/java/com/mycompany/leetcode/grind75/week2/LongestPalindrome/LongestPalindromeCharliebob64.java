package com.mycompany.leetcode.grind75.week2.LongestPalindrome;

import java.util.HashSet;

public class LongestPalindromeCharliebob64 {
    public int longestPalindrome(String s) {
        if(s == null || s.length() == 0) return 0;
        HashSet<Character> hs = new HashSet<Character>();
        int count = 0;
        for(int i = 0; i < s.length(); i++) {
            if(hs.contains(s.charAt(i))) {
                hs.remove(s.charAt(i));
                count++;
            } else {
                hs.add(s.charAt(i));
            }
        }
        if(!hs.isEmpty()) return count * 2 + 1;
        return count * 2;
    }

    public static void main(String[] args) {
        String s = "abccccdd";
        LongestPalindromeCharliebob64 obj = new LongestPalindromeCharliebob64();
        System.out.println(obj.longestPalindrome(s));
    }
}
