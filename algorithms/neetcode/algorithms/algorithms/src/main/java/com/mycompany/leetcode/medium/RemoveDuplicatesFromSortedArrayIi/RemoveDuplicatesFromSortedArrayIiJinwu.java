package com.mycompany.leetcode.medium.RemoveDuplicatesFromSortedArrayIi;

import javax.print.DocFlavor;

public class RemoveDuplicatesFromSortedArrayIiJinwu {
    public int removeDuplicates(int[] nums) {
        if(nums.length < 2) {
            return nums.length;
        }

        int i = 0, len = 0;
        while(i < nums.length) {
            if(len < i) {
                nums[len++] = nums[i++];
            } else {
                i++;
                len++;
            }

            int j = i;
            while(j < nums.length && nums[j] == nums[i - 1]) {
                j++;
            }
            if(j - i > 0) {
                nums[len++] = nums[i++];
            }
            i = j;
        }
        return len;
    }

    public static void main(String[] args) {
        RemoveDuplicatesFromSortedArrayIiJinwu S = new RemoveDuplicatesFromSortedArrayIiJinwu();
        System.out.println(S.removeDuplicates(new int[] {1, 1, 1, 2}));
    }
}
