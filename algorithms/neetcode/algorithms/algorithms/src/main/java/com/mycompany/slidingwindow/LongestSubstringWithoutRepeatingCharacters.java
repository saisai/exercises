package com.mycompany.slidingwindow;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class LongestSubstringWithoutRepeatingCharacters {

    public static int lengthOfLongestSubstring(String s) {

        List<Character> subStringL = new ArrayList<>();
        int largestLength = 0;

        for(int right = 0; right < s.length(); right++) {
            if(subStringL.contains(s.charAt(right))) {
                // get the index of the cahr
                int index = subStringL.indexOf(s.charAt(right));
                subStringL.remove(index);
                if(index > 0) {
                    subStringL.subList(0, index).clear();
                }
            }
            subStringL.add(s.charAt(right));
            largestLength = Math.max(largestLength, subStringL.size());
        }
        return largestLength;
    }

    public static void main(String[] args) {
        String s = "abcabcbb";
        System.out.println(lengthOfLongestSubstring(s));
    }

}
