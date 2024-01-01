package com.mycompany.leetcode.grind75.week6.WordBreak;

import java.util.*;

public class WordBreakRocky_zhang {
    private boolean wb(String s, Set<String> set) {
        int len = s.length();
        if(len == 0) {
            return true;
        }
        for(int i = 1; i <= len; i++) {
            if(set.contains(s.substring(0, i)) && wb(s.substring(i), set)) {
                return true;
            }
        }
        return false;
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        return wb(s, set);
    }

    public static void main(String[] args) {
        String s = "leetcode";
        List<String> wordDict = Arrays.asList(new String[] {"leet","code"});
        WordBreakRocky_zhang obj = new WordBreakRocky_zhang();
        System.out.println(obj.wordBreak(s, wordDict));
    }
}
