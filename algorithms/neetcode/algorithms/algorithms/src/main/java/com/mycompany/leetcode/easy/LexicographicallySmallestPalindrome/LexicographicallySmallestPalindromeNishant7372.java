package com.mycompany.leetcode.easy.LexicographicallySmallestPalindrome;

public class LexicographicallySmallestPalindromeNishant7372 {
    static String makeSmallestPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        char[] arr = s.toCharArray();
        while(i <= j) {
            if(arr[i] != arr[j]) {
                arr[i] = arr[j] = (char) Math.min(arr[i], arr[j]);
            }
            i++;
            j--;
        }
        return new String(arr);
    }

    public static void main(String[] args) {
        String s = "egcfe";
        System.out.println(makeSmallestPalindrome(s));
    }
}
