/*
 * 
 * https://leetcode.com/problems/cyclically-rotating-a-grid/discuss/1299543/Java-solution-mocking-rotation-by-Queue
 * https://leetcode.com/problems/cyclically-rotating-a-grid/
 * 
 * // The layer will recover after few rounds of cyclic rotations.
// So the effective rotations for Each layer is k % length_of_layer.
// To mock the process of rotations, we could use Queue.
 */

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solutiondotflyoceans {

    public static void main(String[] args){

        Solutiondotflyoceans S = new Solutiondotflyoceans();
        int[][] grid = {{40,10},{30,20}};
        int k = 1;
        System.out.println(Arrays.toString( S.roateGrid(grid, k)));

    }

    public int[][] roateGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;

        for(int i = 0; i < Math.min(m/2, n/2); i++) {
            int div = (m - i * 2) * 2 + (n - i*2 - 2) * 2;
            rotate(grid, i, i, k%div);
        }
        return grid;
    }

    public int[][] rotateGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        
        for (int i = 0; i < Math.min(m/2, n/2); i++) {
            int div = (m - i*2)*2 + (n - i*2 -2)*2;
            rotate(grid, i, i, k%div);
        }
        return grid;
    }
    
    public void rotate(int[][] matrix, int row, int col, int k) {
        Queue<Integer> list = new LinkedList<>();
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = col; i <= n-col-1; i++) list.add(matrix[row][i]);
        for (int i = row+1; i <= m-row-1-1; i++) list.add(matrix[i][n-col-1]);
        for (int i = n-col-1; i >= col; i--) list.add(matrix[m-row-1][i]);
        for (int i = m-row-1-1; i >= row+1; i--) list.add(matrix[i][col]);
        
        // cyclic rotate k times.
        while (k > 0) {
            int tmp = list.poll();
            list.add(tmp);
            k--;
        }
        
        for (int i = col; i <= n-col-1; i++) matrix[row][i] = list.poll();
        for (int i = row+1; i <= m-row-1-1; i++) matrix[i][n-col-1] = list.poll();
        for (int i = n-col-1; i >= col; i--) matrix[m-row-1][i] = list.poll();
        for (int i = m-row-1-1; i >= row+1; i--) matrix[i][col] = list.poll();
        
    }

    /*
    public void rotate(int[][] matrix, int row, int col, int k) {
        Queue<Integer> list = new LinkedList<>();
        int m = matrix.length;
        int n = matrix[0].length;
        for(int i = col; i < n-col-1; i++) list.add(matrix[row][i]);
        for(int i = row + 1; i <= m-row-1-1; i++) list.add(matrix[i][n-col-1]);
        for(int i= n-col-1; i >= col; i--) list.add(matrix[m-row-1][i]);
        for(int i=m-row-1-1; i >= row+1; i--) list.add(matrix[i][col]);


        // cyclic roate k times.
        while(k > 0) {
            int tmp = list.poll();
            list.add(tmp);
            k--;
        }

        for(int i=col; i <= n-col-1;i++) matrix[row][i] = list.poll();
        for(int i=row+1; i<=m-row-1-1; i++) matrix[i][n-col-1] = list.poll();
        for(int i= n-col-1; i >=col; i--)  matrix[m-row-1][i] = list.poll();
        for(int i =m-row-1-1; i >= row+1; i--) matrix[i][col] = list.poll();
    }
    */
}