package com.mycompany.leetcode.hard.DistinctEchoSubstrings;

import java.util.HashSet;
import java.util.Set;

public class DistinctEchoSubstringsChappy1 {

    static class RollingHash {
        int n;
        int base = 31;
        long[] p;
        long[] h;

        public RollingHash(String text) {
            n = text.length();
            p = new long[n + 2];
            h = new long[n + 2];

            p[0] = 1;

            for (int i = 1; i <= n; i++) {
                p[i] = p[i - 1] * base;
                h[i] = h[i - 1] * base + text.charAt(i - 1);
            }
        }

        public long get(int l, int r) {
            return h[r] - h[l - 1] * p[r - l + 1];
        }
    }

    static int distinctEchoSubstrings(String text) {
        Set<Long> st = new HashSet<>();
        RollingHash rh = new RollingHash(text);
        for(int i = 0; i < text.length(); i++){
            for(int j = i; j < text.length(); j++){
                if( (j-i+1) % 2 == 0){
                    int mid = (i+1)+(j+1-(i+1))/2;
                    if(rh.get(i+1, mid) == rh.get(mid+1, j+1)){
                        st.add(rh.get(i+1, j+1));
                    }
                }
            }
        }
        return st.size();
    }

    public static void main(String[] args) {
        String text = "abcabcabc";
        System.out.println(distinctEchoSubstrings(text));
    }

}
