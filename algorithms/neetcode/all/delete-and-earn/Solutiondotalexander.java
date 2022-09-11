/*
 * https://leetcode.com/problems/delete-and-earn
 * https://leetcode.com/problems/delete-and-earn/discuss/109895/JavaC%2B%2B-Clean-Code-with-Explanation
 * 
 * If we sort all the numbers into buckets indexed by these numbers, this is essentially asking you to repetitively take an bucket while giving up the 2 buckets next to it. (the range of these numbers is [1, 10000])

The optimal final result can be derived by keep updating 2 variables skip_i, take_i, which stands for:
skip_i : the best result for sub-problem of first (i+1) buckets from 0 to i, while you skip the ith bucket.
take_i : the best result for sub-problem of first (i+1) buckets from 0 to i, while you take the ith bucket.

DP formula:
take[i] = skip[i-1] + values[i];
skip[i] = Math.max(skip[i-1], take[i-1]);
take[i] can only be derived from: if you skipped the [i-1]th bucket, and you take bucket[i].
skip[i] through, can be derived from either take[i-1] or skip[i-1], whatever the bigger;

/**
 * for numbers from [1 - 10000], each has a total sum sums[i]; if you earn sums[i], you cannot earn sums[i-1] and sums[i+1]
 * kind of like house robbing. you cannot rob 2 connected houses.
 * 
 */

import java.util.ArrayList;
import java.util.List;

class Solutiondotalexander {

    public static void main(String[] args) {

        
        
        int[][] myNumbers = { {3,4,2}, {2,2,3,3,3,4} };


        for (int i = 0; i < myNumbers.length; ++i) {
            System.out.println(myNumbers[i].toString());
            Solutiondotalexander S = new Solutiondotalexander();
            System.out.println(S.deleteAndEarn(myNumbers[i]));
         }

        
    
        //int[] nums = {3,4,2};
        //Solutiondotalexander S = new Solutiondotalexander();
        //System.out.println(S.deleteAndEarn(nums));
        

    }

    public int deleteAndEarn(int[] nums) {
        int n = 10001;
        int[] values = new int[n];
        for(int num : nums) {
            values[num] += num;
        }

        int take = 0, skip = 0;
        for(int i= 0; i < n; i++) {
            int takei = skip + values[i];
            int skipi = Math.max(skip, take);
            take = takei;
            skip = skipi;
        }
        return Math.max(take, skip);
    }
}