package com.mycompany.leetcode.easy.FindNumbersWithEvenNumberOfDigits;

public class FindNumbersWithEvenNumberOfDigitsChappy1 {

    static int findNumbers(int[] nums) {
        int output = 0;
        for(int number : nums) {
            if(number == 100000) output++;
            else if (number > 10000) output += 0;
            else if(number >= 1000) output++;
            else if(number >= 100) output += 0;
            else if(number >= 10) output++;
        }
        return output;
    }

    public static void main(String[] args) {
        int[] nums = {12,345,2,6,7896};
        System.out.println(findNumbers(nums));
    }
}
