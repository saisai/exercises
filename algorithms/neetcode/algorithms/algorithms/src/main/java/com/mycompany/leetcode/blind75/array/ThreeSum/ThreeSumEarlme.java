package com.mycompany.leetcode.blind75.array.ThreeSum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSumEarlme {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        for(int i = 0; i < nums.length - 2; i++) {
            if(i > 0 && (nums[i] == nums[i-1])) continue;
            for(int j = i +1, k = nums.length - 1; j < k;) {
                if(nums[i] + nums[j] + nums[k] == 0) {
                    list.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++; k--;
                    while((j < k) && (nums[j] == nums[j-1])) j++;
                    while((j < k) && (nums[k] == nums[k+1])) k--;
                } else if(nums[i] + nums[j] + nums[k] > 0) k--;
                else j++;
            }
        }
        return list;
    }

    public static void main(String[] args) {
        int[] nums = {-1,0,1,2,-1,-4};
        ThreeSumEarlme obj = new ThreeSumEarlme();
        List<List<Integer>> result = obj.threeSum(nums);
        System.out.println(Arrays.deepToString(result.toArray()));
    }
}
