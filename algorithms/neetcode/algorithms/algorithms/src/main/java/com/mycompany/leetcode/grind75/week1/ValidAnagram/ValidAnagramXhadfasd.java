package com.mycompany.leetcode.grind75.week1.ValidAnagram;

import com.mycompany.leetcode.grind75.week1.ValidPalindrome.ValidPalindromeSakshamkaushiik;

public class ValidAnagramXhadfasd {
    public boolean isAnagram(String s, String t) {
        int[] alphabet = new int[26];
        for(int i = 0; i < s.length(); i++) alphabet[s.charAt(i) - 'a']++;
        for(int i = 0; i < t.length(); i++) alphabet[t.charAt(i) - 'a']--;
        for(int i : alphabet) if(i != 0) return false;
        return true;
    }

    public static void main(String[] args) {
        ValidAnagramXhadfasd obj = new ValidAnagramXhadfasd();
        String s = "anagram", t = "nagaram";
        String[][] tt = {{"anagram", "nagaram"},
                {"rat", "car"}
                        };
        System.out.println(obj.isAnagram(s ,t ));
        for(String[] a : tt) {
            System.out.println(obj.isAnagram(a[0], a[1]));
        }
    }
}
