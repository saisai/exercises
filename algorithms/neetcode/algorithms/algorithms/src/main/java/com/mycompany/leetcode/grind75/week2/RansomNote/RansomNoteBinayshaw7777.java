package com.mycompany.leetcode.grind75.week2.RansomNote;

public class RansomNoteBinayshaw7777 {
    public boolean canConstruct(String ransomNote, String magazine) {
        if(ransomNote.length() > magazine.length()) return false;
        int[] alphabets_counter = new int[26];

        for(char c : magazine.toCharArray()) {
            alphabets_counter[c-'a']++;
        }

        for(char c: ransomNote.toCharArray()) {
            if(alphabets_counter[c-'a'] == 0) return false;
            alphabets_counter[c-'a']--;
        }

        return true;
    }

    public static void main(String[] args) {
        RansomNoteBinayshaw7777 obj = new RansomNoteBinayshaw7777();
        String ransomNote = "aa", magazine = "aab";
        System.out.println(obj.canConstruct(ransomNote, magazine));
    }
}
