package com.mycompany.leetcode.grind75.week7.FindAllAnagramsInAString;

import java.util.ArrayList;
import java.util.List;

public class FindAllAnagramsInAStringHimalik {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list = new ArrayList<Integer>();
        if(p.length() > s.length()) return list;

        int N = s.length();
        int M = p.length();
        int[] count = freq(p);

        int[] currentCount = freq(s.substring(0, M));

        if(areSame(count,currentCount)) // areSame function
            list.add(0);

        int i;
        for(i=M; i < N; i++) {
            currentCount[s.charAt(i-M) - 'a']--;
            currentCount[s.charAt(i)-'a']++;
            if(areSame(count, currentCount)) {
                list.add(i-M+1);
            }
        }
        return list;
    }

    private boolean areSame(int[] x, int[] y) {
        for(int i = 0; i < 26; i++) {
            if(x[i] != y[i])
                return false;
        }
        return true;
    }

    private int[] freq(String s) {
        int[] count = new int[26];

        for(int i = 0; i < s.length(); i++){
            count[s.charAt(i) - 'a']++; // update acc. to it's frequency
        }
        return count; // and return count
    }

    public static void main(String[] args) {
        FindAllAnagramsInAStringHimalik obj = new FindAllAnagramsInAStringHimalik();
        String s = "cbaebabacd", p = "abc";
        List<Integer> results = obj.findAnagrams(s, p);
        results.forEach(lst -> {
            System.out.println(lst);
        });
    }

}
