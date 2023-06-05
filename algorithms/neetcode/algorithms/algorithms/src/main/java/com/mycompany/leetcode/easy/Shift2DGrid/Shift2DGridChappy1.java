package com.mycompany.leetcode.easy.Shift2DGrid;

import java.util.Arrays;
import java.util.List;

public class Shift2DGridChappy1 {
    static List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int rowCount = grid.length;
        int colCount = grid[0].length;
        int gridCount = rowCount * colCount;
        k = k % gridCount;
        int kCol = (gridCount - k) % colCount;
        int kRow = ((gridCount - k) % gridCount) / colCount;
        int[] innRow = grid[kRow];
        int[][] result = new int[rowCount][colCount];
        for (int r = 0; r < rowCount; r++) {
            int[] outRow = result[r];
            for (int c = 0; c < colCount; c++) {
                outRow[c] = innRow[kCol];
                if (++kCol >= colCount) {
                    kCol = 0;
                    if (++kRow >= rowCount)
                        kRow = 0;
                    innRow = grid[kRow];
                }
            }
        }
        return (List)Arrays.asList(result);
    }

    public static void main(String[] args) {
        int[][] grid = {{1,2,3},{4,5,6},{7,8,9}};
        int k = 1;

        Arrays.stream(grid).forEach((i) -> {
            Arrays.stream(i).forEach((j) -> System.out.print(j + " "));
            System.out.println();
        });

        List<List<Integer>> result = shiftGrid(grid, 1);

        int row = result.size();

        System.out.println(row);
        for(int i = 0; i < row; i++) {
            System.out.println(result.get(i).toArray());

        }


    }
}
