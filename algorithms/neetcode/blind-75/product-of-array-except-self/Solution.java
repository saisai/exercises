/*
 *https://leetcode.com/problems/product-of-array-except-self/discuss/1342916/3-Minute-Read-Mimicking-an-Interview
	//
	//https://leetcode.com/problems/product-of-array-except-self/
 */
class Solution {

	public static void main(String[] args){
		
		int[] nums = {1,2,3,4};
		int[] result = productExceptSelf(nums);
		System.out.println(result);

	}
	
	public static int[] productExceptSelf(int[] nums) {
		int n = nums.length;
		int ans[] = new int[n];

		for(int i=0; i < n; i++) {
			int pro = 1;
			for (int j = 0; j < n; j++){
				if(i == j) continue;
				pro *= nums[j];
			}
			ans[i] = pro;
		}

		return ans;
	}

}
