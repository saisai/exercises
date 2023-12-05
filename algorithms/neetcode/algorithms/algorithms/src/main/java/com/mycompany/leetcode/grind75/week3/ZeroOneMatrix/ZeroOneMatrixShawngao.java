package com.mycompany.leetcode.grind75.week3.ZeroOneMatrix;

import java.util.*;
import java.util.stream.Collectors;

public class ZeroOneMatrixShawngao {
    public List<List<Integer>> updateMatrix(List<List<Integer>> matrix) {
        int m = matrix.size();
        int n = matrix.get(0).size();

        Queue<int[]> queue = new LinkedList<>();
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(matrix.get(i).get(j) == 0) {
                    queue.offer(new int[] {i, j});
                } else {
                    matrix.get(i).set(j, Integer.MAX_VALUE);
                }
            }
        }

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while(!queue.isEmpty()) {
            int[] cell = queue.poll();
            for(int[] d : dirs) {
                int r = cell[0] + d[0];
                int c = cell[1] + d[1];
                if(r < 0 || r >= m || c < 0 || c >= n ||
                    matrix.get(r).get(c) <= matrix.get(cell[0]).get(cell[1]) + 1) continue;
                queue.add(new int[] {r, c});
                matrix.get(r).set(c, matrix.get(cell[0]).get(cell[1])  + 1);
            }
        }
        return matrix;
    }

    public int[][] updateMatrix2(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    queue.offer(new int[] {i, j});
                }
                else {
                    matrix[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int[] d : dirs) {
                int r = cell[0] + d[0];
                int c = cell[1] + d[1];
                if (r < 0 || r >= m || c < 0 || c >= n ||
                        matrix[r][c] <= matrix[cell[0]][cell[1]] + 1) continue;
                queue.add(new int[] {r, c});
                matrix[r][c] = matrix[cell[0]][cell[1]] + 1;
            }
        }

        return matrix;
    }

    public static void main(String[] args) {
        int[][] mat = {{0,0,0},{0,1,0},{1,1,1}};
        ZeroOneMatrixShawngao obj = new ZeroOneMatrixShawngao();
        int[][] results = obj.updateMatrix2(mat);
        for(int[] m : results) {
            System.out.println(Arrays.toString(m));
        }
//        List<List<Integer>> results = new ArrayList<>();
//        for(int[] m : mat) {
//            System.out.println(Arrays.toString(m));
//            results.add(new ArrayList<Integer>(Arrays.asList(m)));
//        }

    }
}
