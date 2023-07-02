package com.mycompany.leetcode.medium.WordBreak;

import java.util.Arrays;
import java.util.List;

public class WordBreakTlj77 {
    private boolean wordBreak(String s, int startIndex, List<String> wordDict, boolean[] visited) {
        if(startIndex == s.length()) return true;
        if(visited[startIndex]) return false;
        visited[startIndex] = true;
        for(String word : wordDict) {
            if(s.startsWith(word, startIndex)) {
                if(wordBreak(s, startIndex+word.length(), wordDict, visited)) return true;
            }
        }
        return false;
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] visited = new boolean[s.length()];
        return wordBreak(s, 0, wordDict, visited);
    }

    public static void main(String[] args) {
        WordBreakTlj77 obj = new WordBreakTlj77();
        String s = "leetcode";
        String[] wordDict = {"leet","code"};
        List<String> wordList = Arrays.asList(wordDict);
        System.out.println(obj.wordBreak(s, wordList));
    }
}

// https://stackoverflow.com/questions/6026813/converting-string-array-to-java-util-list
// https://leetcode.com/problems/word-break/solutions/435196/java-very-simple-dfs-method-beat-100/
