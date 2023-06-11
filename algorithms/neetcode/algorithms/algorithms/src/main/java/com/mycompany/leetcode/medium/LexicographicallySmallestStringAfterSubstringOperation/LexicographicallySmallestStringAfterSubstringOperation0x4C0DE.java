package com.mycompany.leetcode.medium.LexicographicallySmallestStringAfterSubstringOperation;

public class LexicographicallySmallestStringAfterSubstringOperation0x4C0DE {

    static String smallestString(String s) {
        final int n = s.length();
        StringBuilder sb = new StringBuilder();
        int index = 0;
        char c;

        // skip all leading 'a'
        while(index < n && (c = s.charAt(index)) == 'a') {
            sb.append(c);
            index++;
        }

        // all characters are 'a'
        if(index == n) {
            sb.deleteCharAt(n - 1);
            sb.append('z');
            return sb.toString();
        }

        // perform the operation
        while(index < n && (c = s.charAt(index)) != 'a') {
            sb.append((char) ((c - 'a' - 1 + 26) % 26 + 'a'));
            index++;
        }

        // stop at second 'a'
        while(index < n) {
            sb.append(s.charAt(index));
            index++;
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        String s = "cbabc";
        System.out.println(smallestString(s));
    }
}
