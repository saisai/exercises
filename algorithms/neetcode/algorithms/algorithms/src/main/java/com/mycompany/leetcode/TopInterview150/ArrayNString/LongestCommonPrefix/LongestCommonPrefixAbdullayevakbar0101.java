package com.mycompany.leetcode.TopInterview150.ArrayNString.LongestCommonPrefix;

import java.util.Arrays;
import java.util.Map;

public class LongestCommonPrefixAbdullayevakbar0101 {
    public String longestCommonPrefix(String[] v) {
        StringBuilder ans = new StringBuilder();
        Arrays.sort(v);
        String first = v[0];
        String last = v[v.length-1];
        for(int i = 0; i < Math.min(first.length(), last.length()); i++) {
            if(first.charAt(i) != last.charAt(i)) {
                return ans.toString();
            }
            ans.append(first.charAt(i));
        }
        return ans.toString();
    }

    public static void main(String[] args) {
        LongestCommonPrefixAbdullayevakbar0101 obj = new LongestCommonPrefixAbdullayevakbar0101();
        String[] strs = {"flower","flow","flight"};
        System.out.println(obj.longestCommonPrefix(strs));
    }
}
