package com.mycompany.leetcode.randomly.dfs;

public class ArrayNestinghelloworldzt {
    private int calcLength(int[] nums, int start, boolean[] visited) {
        int i = start, count = 0;
        while(count == 0 || i != start){
            visited[i] = true;
            i = nums[i];
            count++;
        }
        return count;
    }

    public int arrayNesting(int[] nums) {
        int max = Integer.MIN_VALUE;
        boolean[] visited = new boolean[nums.length];
        for(int i = 0; i < nums.length; i++) {
            if(visited[i])
                continue;
            max = Math.max(max, calcLength(nums, i, visited));
        }
        return max;
    }

    public static void main(String[] args) {
        int[] nums = {5,4,0,3,1,6,2};
        ArrayNestinghelloworldzt obj = new ArrayNestinghelloworldzt();
        System.out.println(obj.arrayNesting(nums));
    }
}
