/*
 * https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
 * https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/discuss/1267411/Java-Solution-using-binary-Search-with-Explanation
 * 
 */
class Solution {

    public static void main(String[] args){        
        /* 
        int[] chalk = {5, 1, 5};
        int k = 22;
        */
        int[] chalk = {3,4,1,2};
        int k = 25;
        Solution s = new Solution();
        System.out.println(s.chalkReplacer(chalk, k));

    }

    public int chalkReplacer(int[] chalk, int s){

        long k = s;
        long[] prefix = new long[chalk.length];
        prefix[0] = chalk[0];
        for(int i=1; i < chalk.length; i++) {
            prefix[i] = chalk[i] + prefix[i-1];
        }

        if(prefix[chalk.length-1] <= k) {
            k = k % prefix[chalk.length-1];
        }

        if(k==0) return 0;

        int i = 0;
        int j = chalk.length - 1;

        while(i <= j) {
            int mid = i + (j-i) / 2;

            if(k - prefix[mid] == 0) return mid + 1;
            else if(k - prefix[mid] < 0) {
                j = mid - 1;
            } else {
                i = mid + 1;
            }
        }
        return i;
    }
}