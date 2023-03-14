package com.mycompany.slidingwindow;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class RepeatedDnaSequences {
    private static List<String> findRepeatedDnaSequences(String s) {
        HashSet<String> set = new HashSet<>();
        int start = 0;
        HashSet<String> ans = new HashSet<>();
        for(int end = 10; end <= s.length(); end++) {
            if(set.contains(s.substring(start, end))) ans.add(
                    s.substring(start, end)
            );
            set.add(s.substring(start,end));
            start++;
        }
        List<String> list = new ArrayList<>(ans);
        return list;
    }

    public static void main(String... args) {
        String s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
        System.out.print(findRepeatedDnaSequences(s));
    }
}
