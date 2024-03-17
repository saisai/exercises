package com.mycompany.leetcode.TopInterview150.HashMap.ValidAnagram;

public class ValidAnagramaRahulvarma5297 {
    public boolean isAnagram(String s, String t) {
        int[] count = new int[26];

        for(char x : s.toCharArray()) {
            count[x - 'a']++;
        }

        for(char x : t.toCharArray()) {
            count[x - 'a']--;
        }

        for(int val : count) {
            if(val != 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        ValidAnagramaRahulvarma5297 obj = new ValidAnagramaRahulvarma5297();
        String s = "anagram", t = "nagaram";
        System.out.println(obj.isAnagram(s, t));
    }
}
