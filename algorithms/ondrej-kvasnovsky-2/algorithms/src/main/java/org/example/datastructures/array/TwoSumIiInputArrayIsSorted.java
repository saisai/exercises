package org.example.datastructures.array;

import java.util.Arrays;

public class TwoSumIiInputArrayIsSorted {
    public int[] twoSum(int[] numbers, int target) {
        // use binary search
        int index1 = 0;
        int index2 = 0;
        for(int i = 0; i < numbers.length; i++) {
            int val = numbers[i];
            int found = Arrays.binarySearch(numbers, i  + 1, numbers.length, target - val);
            if(found >= 0) {
                index1 = i + 1;
                index2 = found + 1;
                break;
            }
        }
        return new int[]{index1, index2};
    }

    public int[] twoSumTwoPointer(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;
        while(start < end) {
            int sum = numbers[start] + numbers[end];
            if(sum == target) {
                return new int[]{start + 1, end + 1};
            }
            if(sum > target) {
                end--;
            } else {
                start++;
            }
        }
        return new int[]{ -1, -1};
    }

    public static void main(String[] args) {
        TwoSumIiInputArrayIsSorted obj = new TwoSumIiInputArrayIsSorted();
        int[] numbers = {2,7,11,15};
        int target = 9;
        int[] result = obj.twoSum(numbers, target);
        System.out.println(Arrays.toString(result));
        System.out.println(Arrays.toString(obj.twoSumTwoPointer(numbers, target)));

    }
}

// https://ondrej-kvasnovsky-2.gitbook.io/algorithms/data-structures/array/two-sum-ii-input-array-is-sorted