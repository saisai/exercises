package com.mycompany.leetcode.grind75.week8.LargestRectangleInHistogram;

import java.util.Stack;

public class LargestRectangleInHistogramJeantimex {
    public int largestRectangleArea(int[] h) {
        int n = h.length, i = 0, max = 0;

        Stack<Integer> s = new Stack<>();
        while(i < n) {
            while(!s.isEmpty() && h[i] < h[s.peek()]) {
                max = Math.max(max, h[s.pop()] * (i - (s.isEmpty() ? 0 : s.peek() + 1)));
            }
            s.push(i++);
        }

        while(!s.isEmpty()) {
            max = Math.max(max, h[s.pop()] * (n - (s.isEmpty() ? 0 : s.peek() + 1)));
        }

        return max;
    }

    public static void main(String[] args) {
        LargestRectangleInHistogramJeantimex obj = new LargestRectangleInHistogramJeantimex();
        int[] heights = {2,1,5,6,2,3};
        System.out.println(obj.largestRectangleArea(heights));
    }
}
