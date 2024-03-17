package com.mycompany.leetcode.TopInterview150.HashMap.GroupAnagrams;

import java.util.*;

public class GroupAnagrams150rahulvarma5297 {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for(String word : strs) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);

            if(!map.containsKey(sortedWord)) {
                map.put(sortedWord, new ArrayList<>());
            }

            map.get(sortedWord).add(word);
        }

        return new ArrayList<>(map.values());
    }

    public static void main(String[] args) {
        GroupAnagrams150rahulvarma5297 obj = new GroupAnagrams150rahulvarma5297();
        String[] strs = {"eat","tea","tan","ate","nat","bat"};

        List<List<String>> results = obj.groupAnagrams(strs);

        results.forEach(lst -> {
            System.out.println(lst);
        });
    }
}
