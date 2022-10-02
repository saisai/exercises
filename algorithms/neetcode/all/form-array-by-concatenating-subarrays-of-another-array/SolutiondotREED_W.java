/*
 * 
 * https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
 * https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/discuss/1074665/KMP-Java-O(n%2Bm)
 * 
 */

class SolutiondotREED_W {

    public static void main(String[] args) {

        SolutiondotREED_W S = new SolutiondotREED_W();

        int[][] groups = {{1,-1,-1},{3,-2,0}};
        int[] nums = {1,-1,0,1,-1,-1,3,-2,0};

        System.out.println(S.sln2(groups, nums));

    }

    private boolean sln2(int[][] groups, int[] nums){
        int n = groups.length;
        int m = nums.length;
        
        int[][] prefixes = new int[n][];
        for(int i = 0;i<n;i++) prefixes[i] = getPrefix(groups[i]);
        int j = 0;
        for(int i = 0;i< m && j<n;){
            int index = search(nums, groups[j], prefixes[j], i);
            if(index<0) return false;
            j++;
            i = index;
        }
        return j==n;
    }
    
    private int[] getPrefix(int[] arr){
        int n = arr.length;
        int[] res = new int[n];
        for(int i = 1, j =0; i<n;){
            if(arr[i] == arr[j]){
                res[i]  = j+1;
                i++;j++;
            }else if(j>0){
                j = res[j-1];
            }else{
                i++;
            }
        }
        return res;
    }
    
    private int search(int[] arr1, int[] arr2, int[] prefix, int startIndex){
        int m = arr1.length;
        int n = arr2.length;
        for(int i = startIndex, j = 0; i<m;){
            if(arr1[i] == arr2[j]){
                i++;j++;
            }else if(j>0){
                j = prefix[j-1];
            }else{
                i++;
            }
            
            if(j==n) return i;
        }
        return -1;
    }

}