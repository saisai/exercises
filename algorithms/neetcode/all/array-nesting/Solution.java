/*
 * https://leetcode.com/problems/array-nesting/
 * https://leetcode.com/problems/array-nesting/discuss/102432/C%2B%2B-Java-Clean-Code-O(N)
 */
class Solution {
    public static void main(String[] args){

        Solution S = new Solution();
        int[] nums = {5,4,0,3,1,6,2};
        System.out.println(S.arrayNesting(nums));

    }

    public int arrayNesting(int[] a){
        int maxsize = 0;
        for(int i = 0; i < a.length; i++){
            int size = 0;
            for(int k =i; a[k] >= 0; size++) {
                int ak = a[k];
                a[k] = -1; // mark a[k] as visited;
                k = ak;
            }
            maxsize = Integer.max(maxsize, size);
        }
        return maxsize;
    }
}