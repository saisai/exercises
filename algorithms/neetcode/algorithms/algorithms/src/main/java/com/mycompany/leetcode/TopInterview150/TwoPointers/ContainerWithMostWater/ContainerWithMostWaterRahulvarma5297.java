package com.mycompany.leetcode.TopInterview150.TwoPointers.ContainerWithMostWater;

import java.util.Arrays;

public class ContainerWithMostWaterRahulvarma5297 {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while(left < right) {
            int currentArea = Math.min(height[left], height[right]) * (right - left);
            maxArea = Math.max(maxArea, currentArea);

            if(height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        int[] height = {1,8,6,2,5,4,8,3,7};
        ContainerWithMostWaterRahulvarma5297 obj = new ContainerWithMostWaterRahulvarma5297();
        System.out.println(obj.maxArea(height));
    }
}
