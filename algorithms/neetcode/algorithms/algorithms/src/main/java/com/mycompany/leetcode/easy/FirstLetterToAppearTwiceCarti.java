package com.mycompany.leetcode.easy;

import java.util.HashSet;
import java.util.Set;

public class FirstLetterToAppearTwiceCarti {
    private static char repeatedCharacter(String s) {
        Set<Character> cache = new HashSet<>();
        for(char chr : s.toCharArray()) {
            if(cache.contains(chr)) {
                return chr;
            }

            // set that we've seen this before
            cache.add(chr);
        }

        return ' ';
    }

    public static void main(String[] args) {
        String s = "abccbaacz";
        System.out.println(repeatedCharacter(s));
    }
}
