package com.mycompany.leetcode.grind75.week7.ContainerWithMostWater;

public class ContainerWithMostWaterHimalik {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int max = 0;
        while(left < right) {
            int w = right - left;
            int h = Math.min(height[left], height[right]);
            int area = h * w;
            max = Math.max(max, area);
            if(height[left] < height[right]) left++;
            else if(height[left] > height[right]) right--;
            else {
                left++;
                right--;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int[] height = {1,8,6,2,5,4,8,3,7};
        ContainerWithMostWaterHimalik obj = new ContainerWithMostWaterHimalik();
        System.out.println(obj.maxArea(height));
    }
}
