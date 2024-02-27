package com.mycompany.leetcode.TopInterview150.ArrayNString.FindTheIndexOfTheFirstOccurrenceInAString;

public class FindTheIndexOfTheFirstOccurrenceInAStringJeantimex {
    public int strStr(String haystack, String needle) {
        for(int i = 0; ; i++) {
            for(int j = 0; ; j++) {
                if(j == needle.length()) return i;
                if(i + j == haystack.length()) return -1;
                if(needle.charAt(j) != haystack.charAt(i + j)) break;
            }
        }
    }

    public static void main(String[] args) {
        String haystack = "sadbutsad", needle = "sad";
        FindTheIndexOfTheFirstOccurrenceInAStringJeantimex obj = new FindTheIndexOfTheFirstOccurrenceInAStringJeantimex();
        System.out.println(obj.strStr(haystack, needle));
    }
}
