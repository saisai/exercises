package com.mycompany.leetcode.hard.FindAGoodSubsetOfTheMatrix;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;

public class FindAGoodSubsetOfTheMatrixRock {
    static List<Integer> goodSubsetofBinaryMatrix(int[][] grid) {
        int R = grid.length;
        if(R == 1) {
            return IntStream.of(grid[0]).sum() == 0 ? List.of(0) : List.of();
        }

        Map<Integer, Integer> rowIndices = new HashMap<>();
        for(int r = 0, C = grid[0].length; r < R; ++r) {
            int r1 =r, num = IntStream.range(0, C).map(k -> grid[r1][k] << k).sum();
            for(int i = 0; i < 32; ++i) {
                if((i & num) == 0 && rowIndices.containsKey(i)) {
                    return List.of(rowIndices.get(i), r);
                }
            }
            rowIndices.putIfAbsent(num, r);
        }
        return List.of();
    }

    public static void main(String[] args) {

        int[][] grid = {{0,1,1,0},{0,0,0,1},{1,1,1,1}};
        List<Integer> results = goodSubsetofBinaryMatrix(grid);
        results.forEach(e -> System.out.println(e));
    }
}
