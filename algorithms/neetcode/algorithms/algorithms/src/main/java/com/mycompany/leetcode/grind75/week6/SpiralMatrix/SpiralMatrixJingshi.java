package com.mycompany.leetcode.grind75.week6.SpiralMatrix;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SpiralMatrixJingshi {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<Integer>();
        if(matrix.length == 0 || matrix[0].length == 0) return res;

        int top = 0;
        int bottom = matrix.length-1;
        int left = 0;
        int right = matrix[0].length - 1;

        while(true) {
            for(int i = left; i <= right; i++) res.add(matrix[top][i]);
            top++;

            if(left > right || top > bottom) break;

            for(int i = top; i <= bottom; i++) res.add(matrix[i][right]);
            right--;
            if(left > right || top > bottom) break;

            for(int i = right; i >= left; i--) res.add(matrix[bottom][i]);
            bottom--;
            if(left > right || top > bottom) break;

            for(int i = bottom; i >= top; i--) res.add(matrix[i][left]);
            left++;
            if(left > right || top > bottom) break;
        }

        return res;
    }

    public static void main(String[] args) {
        SpiralMatrixJingshi obj = new SpiralMatrixJingshi();
        int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
        List<Integer> results = obj.spiralOrder(matrix);
        results.forEach(lst -> {
//            System.out.println(Arrays.deepToString(new Integer[]{lst}));
            System.out.print(lst);
        });
    }
}
