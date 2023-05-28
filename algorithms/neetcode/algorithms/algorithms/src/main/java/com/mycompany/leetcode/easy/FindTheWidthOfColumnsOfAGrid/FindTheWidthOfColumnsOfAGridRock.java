package com.mycompany.leetcode.easy.FindTheWidthOfColumnsOfAGrid;

import java.util.Arrays;

public class FindTheWidthOfColumnsOfAGridRock {

    static int[] findColumnWidth(int[][] grid) {
        int C = grid[0].length;
        int[] ans = new int[C];
        for(int c = 0, R = grid.length; c < C; ++c) {
            for(int r = 0; r < R; ++r) {
                ans[c] = Math.max(ans[c], Integer.toString(grid[r][c]).length());
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[][] grid = {{1},{22},{333}};
        int[] result = findColumnWidth(grid);
        System.out.println(Arrays.toString(result));
    }

}
