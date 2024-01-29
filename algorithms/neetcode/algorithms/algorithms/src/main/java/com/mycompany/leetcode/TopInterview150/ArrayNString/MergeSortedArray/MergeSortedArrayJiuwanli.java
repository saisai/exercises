package com.mycompany.leetcode.TopInterview150.ArrayNString.MergeSortedArray;

import java.util.Arrays;

public class MergeSortedArrayJiuwanli {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int tail1 = m - 1, tail2 = n - 1, finished = m + n - 1;
        while(tail1 >= 0 && tail2 >= 0) {
            nums1[finished--] = (nums1[tail1] > nums2[tail2]) ?
                    nums1[tail1--] : nums2[tail2--];
        }

        while(tail2 >= 0)  {
            nums1[finished--] = nums2[tail2--];
        }
    }

    public static void main(String[] args) {
        int[] nums1 = {1,2,3,0,0,0};
        int m = 3;
        int[] nums2 = {2,5,6};
        int n = 3;
        MergeSortedArrayJiuwanli obj = new MergeSortedArrayJiuwanli();
        obj.merge(nums1, m, nums2, n);
        System.out.println(Arrays.toString(nums1));

    }
}
