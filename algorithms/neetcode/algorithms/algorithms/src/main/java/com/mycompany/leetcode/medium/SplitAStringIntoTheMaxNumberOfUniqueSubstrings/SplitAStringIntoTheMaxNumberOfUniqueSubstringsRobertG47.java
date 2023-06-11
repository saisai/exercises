package com.mycompany.leetcode.medium.SplitAStringIntoTheMaxNumberOfUniqueSubstrings;

import java.util.HashSet;

public class SplitAStringIntoTheMaxNumberOfUniqueSubstringsRobertG47 {

    static int length = 0;

    // two cases, we're creating new substring, or we're adding to existing;
    private static void backtrack(HashSet<String> set, char[] cs, int start, StringBuilder str) {
        if(start == cs.length) {
            if(!set.contains(String.valueOf(str))) {
                length = Math.max(length, set.size() + 1);
            }
            return;
        }

        if(length > set.size() + cs.length - start) return;

        if(str.length() != 0 && !set.contains(String.valueOf(str))) {
            String s = String.valueOf(str);
            StringBuilder newStr = new StringBuilder();
            set.add(s);
            newStr.append(cs[start]);
            backtrack(set, cs, start + 1, newStr);
            set.remove(s);
            newStr.deleteCharAt(newStr.length() - 1);
        }

        str.append(cs[start]);
        backtrack(set, cs, start + 1, str);
        str.deleteCharAt(str.length() - 1);
    }

    static int maxUniqueSplit(String s) {
        char[] cs = s.toCharArray();
        HashSet<String> set = new HashSet<>();
        backtrack(set, cs, 0, new StringBuilder());
        return length;
    }

    public static void main(String[] args) {
        String s = "ababccc";
        System.out.println(maxUniqueSplit(s));
    }
}
