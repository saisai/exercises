package com.mycompany.leetcode.grind75.week6.LongestPalindromicSubstring;

public class LongestPalindromicSubstringJinwu {
    private int lo, maxLen;

    private void extendPalindrome(String s, int j, int k) {
        while(j >= 0 && k < s.length() && s.charAt(j) == s.charAt(k)) {
            j--;
            k++;
        }
        if(maxLen < k - j - 1) {
            lo = j + 1;
            maxLen = k - j - 1;
        }
    }

    public String longestPalindrome(String s) {
        int len = s.length();
        if(len < 2) {
            return s;
        }

        for(int i = 0; i < len - 1; i++) {
            extendPalindrome(s, i, i);
            extendPalindrome(s, i, i + 1);
        }
        return s.substring(lo, lo + maxLen);
    }

    public static void main(String[] args) {
        LongestPalindromicSubstringJinwu obj = new LongestPalindromicSubstringJinwu();
        String s = "babad";
        System.out.println(obj.longestPalindrome(s));
    }
}
