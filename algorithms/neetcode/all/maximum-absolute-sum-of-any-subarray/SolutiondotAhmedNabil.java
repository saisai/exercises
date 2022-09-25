
/*
 * https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
 * https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052926/Java-Detailed-Solution-easy-to-read-easy-to-understand
 * 
 */
class SolutiondotAhmedNabil {

    public static void main(String[] args) {

        int[] nums = {1,-3,2,3,-4};
        SolutiondotAhmedNabil S = new SolutiondotAhmedNabil();
        System.out.println(S.maxAbsoluteSum(nums));

    }

    public int maxAbsoluteSum(int[] nums) {
        int posAns = 0;
        int cur = 0;
        for(int i=0; i < nums.length; i++) {
            if(cur + nums[i] > 0) cur += nums[i];
            else cur = 0;
            posAns = Math.max(posAns, cur);
        }

        int negAns = 0;
        cur = 0;
        for(int i = 0; i < nums.length; i++) {
            if(cur + nums[i] < 0) cur += nums[i];
            else cur = 0;
            negAns = Math.min(negAns, cur);
        }

        return Math.max(posAns, -negAns);
    }
}