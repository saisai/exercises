package com.mycompany.leetcode.blind75.graph.PacificAtlanticWaterFlow;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class PacificAtlanticWaterFlowStar1993DFS {
    int[][] dir = new int[][]{{0,1}, {0, -1}, {1, 0}, {-1, 0}};

    public void dfs(int[][] matrix, boolean[][] visited, int height, int x, int y) {
        int n = matrix.length, m = matrix[0].length;
        if(x < 0 || x >= n || y < 0 || y >= m || visited[x][y] || matrix[x][y] < height) {
            return;
        }
        visited[x][y] = true;
        for(int[] d : dir) {
            dfs(matrix, visited, matrix[x][y], x + d[0], y + d[1]);
        }
    }

    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> res = new LinkedList<>();
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return res;
        }
        int n = matrix.length, m = matrix[0].length;
        boolean[][]pacific = new boolean[n][m];
        boolean[][]atlantic = new boolean[n][m];
        for(int i=0; i<n; i++){
            dfs(matrix, pacific, Integer.MIN_VALUE, i, 0);
            dfs(matrix, atlantic, Integer.MIN_VALUE, i, m-1);
        }
        for(int i=0; i<m; i++){
            dfs(matrix, pacific, Integer.MIN_VALUE, 0, i);
            dfs(matrix, atlantic, Integer.MIN_VALUE, n-1, i);
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (pacific[i][j] && atlantic[i][j])
                    res.add(new int[] {i, j});
        return res;
    }

    public static void main(String[] args) {
        PacificAtlanticWaterFlowStar1993DFS dfs = new PacificAtlanticWaterFlowStar1993DFS();
        int[][] heights = {{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}};
        List<int[]> result = dfs.pacificAtlantic(heights);
        result.forEach( res -> {
            for(int d : res) {
                System.out.print(d);
            }
            System.out.println();
        });
        System.out.println(Arrays.deepToString(result.toArray()));
    }
}
