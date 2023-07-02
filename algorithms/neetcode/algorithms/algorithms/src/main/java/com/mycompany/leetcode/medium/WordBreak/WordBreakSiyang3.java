package com.mycompany.leetcode.medium.WordBreak;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class WordBreakSiyang3 {
    private boolean dfs(String s, int index, Set<String> dict, Set<Integer> set) {
        if(index == s.length()) return true;
        if(set.contains(index)) return false;
        for(int i = index + 1; i <= s.length(); i++) {
            String t = s.substring(index, i);
            if(dict.contains(t)){
                if(dfs(s, i, dict, set))
                    return true;
                else
                    set.add(i);
            }
        }
        set.add(index);
        return false;
    }

    public boolean wordBreak(String s, Set<String> dict) {
        Set<Integer> set = new HashSet<Integer>();
        return dfs(s, 0, dict, set);
    }

    public static void main(String[] args) {
        WordBreakSiyang3 obj = new WordBreakSiyang3();
        String s = "leetcode";
        String[] wordDict = {"leet","code"};
        Set<String> dict = new HashSet<>(Arrays.asList(wordDict));
        System.out.println(obj.wordBreak(s, dict));
    }
}

// https://leetcode.com/problems/word-break/solutions/43819/dfs-with-path-memorizing-java-solution/
// https://stackoverflow.com/questions/3064423/how-to-convert-an-array-to-a-set-in-java
