import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
/*
 * https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/731085/Java-Prefix-sum
 * 
 */
class Solution {

    public static void main(String[] args){

        int[] nums = {1,2,3,4};
        int n = 4, left = 1, right = 5;
        Solution S = new Solution();
        System.out.println(S.rangeSum(nums, n, left, right));
    }
    public int rangeSum(int[] nums, int n, int left, int right){
        long res = 0,  mod = 1_000_000_007, sum = 0;
        List<Long> sums = new ArrayList<>(), pSum = new ArrayList<>(); // sums - all sums of subarrays, pSum - prefix sums;
        pSum.add(0L);
        for(int i = 0; i < n; i++){
            sum += nums[i];
            pSum.add(sum);
            for(int j = 0; j < pSum.size() - 1; j++) sums.add(sum - pSum.get(j));
        }
        Collections.sort(sums);
        while(left <= right) res = (res + sums.get(left++ - 1)) % mod;
        return (int) res;
    }
}