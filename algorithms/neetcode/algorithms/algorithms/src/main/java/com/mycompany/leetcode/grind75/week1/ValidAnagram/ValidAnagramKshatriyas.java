package com.mycompany.leetcode.grind75.week1.ValidAnagram;

import java.util.Arrays;

public class ValidAnagramKshatriyas {
    public boolean isAnagram(String s, String t) {
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }

    public static void main(String[] args) {
        ValidAnagramKshatriyas obj = new ValidAnagramKshatriyas();
        String s = "anagram", t = "nagaram";
        System.out.println(obj.isAnagram(s, t));
    }
}
