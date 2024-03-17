package com.mycompany.leetcode.TopInterview150.HashMap.RansomNote;

import java.util.Arrays;

public class RansomNoteBinayshaw7777 {
    public boolean canConstruct(String ransomNote, String magazine) {
        if(ransomNote.length() > magazine.length()) return false;
        int[] alphabetsCounter = new int[26];

        for(char c : magazine.toCharArray()) {
            alphabetsCounter[c-'a']++;
        }

        for(char c : ransomNote.toCharArray()) {
            if(alphabetsCounter[c-'a'] == 0) return false;
            alphabetsCounter[c-'a']--;
        }
        return true;

    }

    public static void main(String[] args) {
        RansomNoteBinayshaw7777 obj = new RansomNoteBinayshaw7777();
        String ransomNote = "aa", magazine = "aab";
        System.out.println(obj.canConstruct(ransomNote, magazine));

    }
}

