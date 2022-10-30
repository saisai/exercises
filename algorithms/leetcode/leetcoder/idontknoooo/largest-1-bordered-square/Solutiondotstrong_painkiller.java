
/*
 * https://leetcode.com/problems/largest-1-bordered-square/
 * https://leetcode.com/problems/largest-1-bordered-square/discuss/345574/Java-DP-Solution-with-Videos-Explained
 * 
 */
class Solutiondotstrong_painkiller {

    public static void main(String[] args){

        int[][] grid = {{1,1,1},{1,0,1},{1,1,1}};
        Solutiondotstrong_painkiller S = new Solutiondotstrong_painkiller();
        System.out.println(S.largestBorderedSquare(grid));

    }

    public int largestBorderedSquare(int[][] grid) {
        if(grid == null || grid.length == 0) return 0;
        int m = grid.length, n = grid[0].length;
        int[][][] dp = new int[m+1][n+1][2];
        int max = 0;

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    dp[i+1][j+1][0] = dp[i][j+1][0] + 1;
                    dp[i+1][j+1][1] = dp[i+1][j][1] + 1;

                    int len = Math.min(dp[i+1][j+1][0], dp[i+1][j+1][1]);
                    for(int k = len; k > max; k--) {
                        int len1 = Math.min(dp[i+1 - k + 1][j+1][1], dp[i+1][j+1-k+1][0]);
                        if(len1 >= k) {
                            max = Math.max(max, k);
                        }
                    }
                } else {
                    dp[i+1][j+1][0] = 0;
                    dp[i+1][j+1][1] = 0;
                }
            }
        }
        return max * max;
    }

}