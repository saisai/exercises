package com.mycompany.leetcode.easy.GreatestCommonDivisorOfStrings;

public class GreatestCommonDivisorOfStringsChappy1 {
    static String mod(String s1, final  String s2) {
        while(s1.startsWith(s2))
            s1 = s1.substring(s2.length());
        return s1;
    }

    static String gcdOfStrings(String str1, String str2) {
        if(str1.length() < str2.length())
            return gcdOfStrings(str2, str1);
        if(!str1.startsWith(str2))
            return "";
        if(str2.isEmpty())
            return str1;
        return gcdOfStrings(str2, mod(str1, str2));
    }

    public static void main(String[] args) {
        String str1 = "ABCABC", str2 = "ABC";
        System.out.println(gcdOfStrings(str1, str2));
    }
}
