// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/solutions/3521907/dp/

package com.mycompany.leetcode.medium;

public class MaximumNumberOfMovesInAGridYadavharsha50 {

    private static int maxMoves(int[][] grid) {
        int dp[][] = new int[grid.length][grid[0].length];
        int max = 0;
        for(int i = 1; i < grid[0].length; i++) {
            for(int j = 0 ; j < grid.length; j++) {
                if(grid[j][i-1] < grid[j][i]) {
                    if(i == 1 || dp[j][i-1] >0) dp[j][i] = Math.max(dp[j][i], 1+dp[j][i-1]);
                }

                if(j-1 >= 0 && grid[j-1][i-1] < grid[j][i]) {
                    if(i == 1 || dp[j-1][i-1] > 0) dp[j][i] = Math.max(dp[j][i], 1 + dp[j-1][i-1]);
                }

                if(j + 1 < grid.length && grid[j+1][i-1] < grid[j][i]) {
                    if(i == 1 || dp[j+1][i-1] > 0) dp[j][i] = Math.max(dp[j][i], 1 + dp[j+1][i-1]);
                }

                max = Math.max(max, dp[j][i]);
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int[][] grid = {{2,4,3,5},{5,4,9,3},{3,4,2,11},{10,9,13,15}};
        System.out.println(maxMoves(grid));
    }

}
