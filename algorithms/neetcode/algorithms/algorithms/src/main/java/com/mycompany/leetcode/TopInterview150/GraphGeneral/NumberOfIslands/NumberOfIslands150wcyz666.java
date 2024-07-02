package com.mycompany.leetcode.TopInterview150.GraphGeneral.NumberOfIslands;

public class NumberOfIslands150wcyz666 {

    private int n, m;
    private void DFSMarking(char[][] grid, int i, int j) {
        if(i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != '1') return;
        grid[i][j] = '0';
        DFSMarking(grid, i + 1, j);
        DFSMarking(grid, i - 1, j);
        DFSMarking(grid, i , j + 1);
        DFSMarking(grid, i , j - 1);
    }

    public int numIslands(char[][] grid) {
        int count = 0;
        n = grid.length;
        if( n == 0) return 0;
        m = grid[0].length;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == '1') {
                    DFSMarking(grid, i, j);
                    ++count;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        NumberOfIslands150wcyz666 obj = new NumberOfIslands150wcyz666();

        char[][] grid = {
                {'1','1','1','1','0'},
                {'1','1','0','1','0'},
                {'1','1','0','0','0'},
                {'0','0','0','0','0'}
        };

        char[][] grid2 = {
                {'1','1','0','0','0'},
                {'1','1','0','0','0'},
                {'0','0','1','0','0'},
                {'0','0','0','1','1'}
        };

        System.out.println(obj.numIslands(grid2));
    }
}
