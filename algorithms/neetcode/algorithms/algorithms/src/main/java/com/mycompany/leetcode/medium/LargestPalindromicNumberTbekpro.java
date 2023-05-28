package com.mycompany.leetcode.medium;

import java.util.Comparator;
import java.util.PriorityQueue;

public class LargestPalindromicNumberTbekpro {
    static String largestPalindromic(String num) {
        int[] digits = new int[10];
        for(int i = 0; i < num.length(); i++) digits[num.charAt(i) - '0']++;
        int countRest = 0;
        for(int i = 1; i < digits.length; i++) countRest += digits[i];
        if(countRest == 0) return "0";
        int highestSingleDigit = -1;
        PriorityQueue<Integer> pqIncr = new PriorityQueue<>(), pqDecr = new PriorityQueue<>(Comparator.reverseOrder());
        for(int i = 0; i < digits.length; i++) {
            if(digits[i] % 2 == 1) highestSingleDigit = i;
            if(digits[i] > 0) {
                for(int j = 0; j < digits[i] / 2; j++) {
                    pqIncr.offer(i);
                    pqDecr.offer(i);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        while(!pqDecr.isEmpty()) sb.append(pqDecr.poll());
        sb.append(highestSingleDigit == -1 ? "" : highestSingleDigit);
        while(!pqIncr.isEmpty()) sb.append(pqIncr.poll());
        int startZero = 0;
        for(int i = 0; i < sb.length(); i++) {
            if(sb.charAt(i) != '0') break;
            startZero++;
        }
        String ans = sb.substring(startZero, sb.length() - startZero);
        return ans;
    }

    public static void main(String[] args) {
        String[] nums = {"444947137",  "00009"};

        for(String num : nums) {
            System.out.println(largestPalindromic(num));
        }
    }
}
