package com.mycompany.neetcode.easy;

import java.lang.reflect.Array;
import java.util.Arrays;

public class TwoSumIIInputArraySsSorted0167 {
    static int[] twoSum(int[] numbers, int target) {
        int aPointer = 0;
        int bPointer = numbers.length - 1;
        int numA, numB;

        while(aPointer < bPointer) {
            numA = numbers[aPointer];
            numB = numbers[bPointer];

            if(numA + numB == target) break;

            if(numA + numB < target) {
                aPointer++;
                continue;
            }

            bPointer--;
        }

        return new int[] { aPointer + 1, bPointer + 1};
    }

    public static void main(String[] args) {
        int[] numbers = {2,7,11,15};
        int target = 9;

        int[] result = twoSum(numbers, target);

        if(result.length > 0) {
            System.out.println(Arrays.toString(result));
        }
    }
}
