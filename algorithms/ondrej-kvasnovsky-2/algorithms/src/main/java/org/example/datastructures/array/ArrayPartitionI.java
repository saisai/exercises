package org.example.datastructures.array;

import java.util.Arrays;

public class ArrayPartitionI {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for(int i = 0; i < nums.length; i += 2) {
            sum += nums[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        ArrayPartitionI obj = new ArrayPartitionI();

        int[] array = {1, 4, 3, 2};
        System.out.println(obj.arrayPairSum(array));
    }
}

// https://ondrej-kvasnovsky-2.gitbook.io/algorithms/data-structures/array/array-partition-i
