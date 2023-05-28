package com.mycompany.leetcode.medium.LongestStringChain;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class LongestStringChainChappy1 {
    static boolean isPredecessor(char[] s, char[] t) {
        for(int i = 0, different = 0; i < s.length; i++) {
            if(s[i] != t[i + different]) {
                if(++different > 1) {
                    return false;
                }
                i--;
            }
        }
        return true;
    }

    static int dfs(List<char[]>[] buckets, char[] parent, int limit) {
        int max = 1;
        for(char[] child : buckets[parent.length - 1]) {
            if(!isPredecessor(child, parent)) {
                continue;
            }

            if((max = Math.max(max, 1 + dfs(buckets, child, limit - 1))) >= limit) {
                return max;
            }
        }
        return max;
    }

    static int longestStrChain(String[] words) {
        List<char[]>[] buckets = new List[17];

        for(int i = 0; i < buckets.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        int smallest = Integer.MAX_VALUE;
        int largest = -1;
        int size;

        for(String w: words) {
            size = w.length();
            smallest = Math.min(smallest, size);
            largest = Math.max(largest, size);
            buckets[size].add(w.toCharArray());
        }
        int max = 1, limit;

        for(int i = largest; i >= smallest; i--) {
            limit = i - smallest + 1;

            for(char[] parent : buckets[i]) {
                if((max = Math.max(max, dfs(buckets, parent, limit))) == limit) {
                    return max;
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        String[] words = {"a","b","ba","bca","bda","bdca"};

        System.out.println(longestStrChain(words));
    }
}
