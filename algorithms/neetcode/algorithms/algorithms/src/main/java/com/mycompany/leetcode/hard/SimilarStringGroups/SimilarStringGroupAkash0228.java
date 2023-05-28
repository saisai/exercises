package com.mycompany.leetcode.hard.SimilarStringGroups;

import java.util.ArrayList;
import java.util.HashSet;

public class SimilarStringGroupAkash0228 {
    static void getAll(String s, ArrayList<String> list, HashSet<String> set) {
        for(int i = 0; i < s.length(); i++) {
            for(int j = i + 1; j < s.length(); j++) {
                if(s.charAt(i) == s.charAt(j))
                    continue;
                String temp = s.substring(0, i) + s.charAt(j) + s.substring(i+1, j) + s.charAt(i) + s.substring(j+1);
                if(set.contains(temp))
                    list.add(temp);
            }
        }
    }

    static void removeAll(String s, HashSet<String> set) {
        set.remove(s);

        ArrayList<String> list = new ArrayList<>();
        getAll(s, list, set);

        for(int j = 0; j < list.size(); j++) {
            removeAll(list.get(j), set);
        }
    }

    static int numSimiliarGroups(String[] strs) {
        HashSet<String> set = new HashSet<>();
        for(String s: strs)
            set.add(s);

        int count = 0;

        for(int i = 0; i < strs.length; i++) {
            if(set.contains(strs[i])) {
                set.remove(strs[i]);
                count++;
                ArrayList<String> list = new ArrayList<>();
                getAll(strs[i], list, set);
                for(int j = 0; j < list.size(); j++) {
                    removeAll(list.get(j), set);
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String[] strs = {"tars","rats","arts","star"};
        System.out.println(numSimiliarGroups(strs));
    }
}
