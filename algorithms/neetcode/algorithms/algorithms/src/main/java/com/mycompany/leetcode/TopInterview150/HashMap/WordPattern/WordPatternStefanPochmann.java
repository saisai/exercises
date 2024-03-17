package com.mycompany.leetcode.TopInterview150.HashMap.WordPattern;

import java.util.HashMap;
import java.util.Map;

public class WordPatternStefanPochmann {
    public boolean wordPattern(String pattern, String str) {
        String[] words = str.split(" ");
        if(words.length != pattern.length())
            return false;
        Map index = new HashMap();
        for(Integer i = 0; i < words.length; i++) {
            if(index.put(pattern.charAt(i), i) != index.put(words[i], i))
                return false;
        }

        return true;
    }

    public static void main(String[] args) {
        String pattern = "abba", s = "dog cat cat dog";
        WordPatternStefanPochmann obj = new WordPatternStefanPochmann();
        System.out.println(obj.wordPattern(pattern, s));
    }
}
