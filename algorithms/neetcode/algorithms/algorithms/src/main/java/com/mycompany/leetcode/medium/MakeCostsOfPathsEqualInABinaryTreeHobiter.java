package com.mycompany.leetcode.medium;

public class MakeCostsOfPathsEqualInABinaryTreeHobiter {
    static int res = 0;
    private static int dfs(int i, int[] cost) {
        if(i > cost.length) return 0;
        int left = dfs(i * 2, cost);
        int right = dfs(i * 2 + 1, cost);

        res += Math.abs(left - right);
        return cost[i - 1] + Math.max(left, right);
    }

    private static int minIncrements(int n, int[] cost) {
        dfs(1, cost);
        return res;
    }

    public static void main(String[] args) {

        int n = 7;
        int[] cost = {1,5,2,2,3,3,1};

        System.out.println(minIncrements(n, cost));

    }
}
