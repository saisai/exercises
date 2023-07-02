package com.mycompany.leetcode.medium.MaximumNumberOfMovesInAGrid;

public class MaximumNumberOfMovesInAGridSolved {

    public int dfs(int[][] grid, int value, int row, int col, int[][] dp) {
        if(row < 0 || row >= grid.length || col < 0 || col >= grid[0].length) {
            return -1;
        }
        if(col != 0 && grid[row][col] <= value) {
            return -1;
        }
        if(dp[row][col] != -1) {
            return dp[row][col];
        }
        dp[row][col] = Math.max(dfs(grid, grid[row][col], row - 1, col + 1, dp), Math.max(dfs(grid, grid[row][col], row, col + 1, dp), dfs(grid, grid[row][col], row + 1, col + 1, dp))) + 1;
        return dp[row][col];
    }

    public int maxMoves(int[][] grid) {
        int[][] dp = new int[grid.length][grid[0].length];
        int maxResult = 0;
        for(int i = 0; i < dp.length; i++) {
            for(int j = 0; j < dp[0].length; j++) {
                dp[i][j] = -1;
            }
        }
        for(int i = 0; i < grid.length; i++) {
            maxResult = Math.max(maxResult, dfs(grid, grid[i][0], i, 0, dp));
        }
        return maxResult;
    }

    public static void main(String[] args) {
        MaximumNumberOfMovesInAGridSolved obj = new MaximumNumberOfMovesInAGridSolved();
        int[][] grid = {{2,4,3,5},{5,4,9,3},{3,4,2,11},{10,9,13,15}};
        System.out.println(obj.maxMoves(grid));

    }
}
