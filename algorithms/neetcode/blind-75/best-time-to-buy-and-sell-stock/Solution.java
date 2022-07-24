
/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1735493/JavaC%2B%2B-best-ever-EXPLANATION-could-possible
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/hi-malik/
*/
class Solution {

	public static void main(String[] args) {
      		System.out.println("Hello, world from Mac!");
		int[] prices = {7,1,5,3,6,4};
		int result = 0;
		result = maxProfit(prices);
		System.out.println(result);

   	}

	public static int maxProfit(int[] prices) {
		int lsf = Integer.MAX_VALUE;
		int op = 0;
		int pist = 0;

		for(int i = 0; i < prices.length; i++) {

			if(prices[i] < lsf) {
				lsf = prices[i];
			}

			pist = prices[i] - lsf;
			if(op < pist) {
				op = pist;
			}

		}
		return op;

	}
}

