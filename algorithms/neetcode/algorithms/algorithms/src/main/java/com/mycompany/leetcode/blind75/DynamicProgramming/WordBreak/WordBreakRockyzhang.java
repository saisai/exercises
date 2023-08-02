package com.mycompany.leetcode.blind75.DynamicProgramming.WordBreak;


import java.util.*;

public class WordBreakRockyzhang {
    static boolean wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>((Collection) wordDict);
        return wb(s, set);
    }

    static boolean wb(String s, Set<String> set) {
        int len = s.length();
        if(len == 0)
            return true;
        for(int i = 0; i <= len; i++) {
            if(set.contains(s.substring(0, i)) && wb(s.substring(i), set)){
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String s = "leetcode";
        String[] wordDict = {"leet","code"};
        List<String> wordDictLst = Arrays.asList(wordDict);
        System.out.println(wordBreak(s, wordDictLst));

    }
}
