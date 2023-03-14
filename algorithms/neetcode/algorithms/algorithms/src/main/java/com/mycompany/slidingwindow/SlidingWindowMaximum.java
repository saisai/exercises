package com.mycompany.slidingwindow;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.stream.IntStream;

public class SlidingWindowMaximum {

    static int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans = new int[nums.length - k + 1];
        int j = 0;
        Deque<Integer> q= new LinkedList<>();
        for(int i = 0 ; i < nums.length; i++) {
            if(!q.isEmpty() && q.peekFirst() < i - k + 1) q.pollFirst();
            while(!q.isEmpty() && nums[i] > nums[q.peekLast()]) q.pollLast();
            q.offer(i);
            if(i >= k - 1) ans[j++] = nums[q.peekFirst()];
        }
        return ans;
    }

    public static void main(String... args) {
        int[] nums = {1,3,-1,-3,5,3,6,7};
        int k = 3;
        // System.out.println(maxSlidingWindow(nums, 3).);
        IntStream stream = Arrays.stream(maxSlidingWindow(nums, 3));
        stream.forEach(str -> System.out.print( str + " "));
    }
}
