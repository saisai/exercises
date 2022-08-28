/*
 * https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
 * https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/discuss/1097359/Java-Dijkstra's-%2B-DFS-%2B-Memoization-%2B-Explanation-of-problem-description
 * 
 * 
 * 
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {

    private Map<Integer, List<int[]>> map = new HashMap<>();
    private final static int mod = 1_000_000_007;
    public static void main(String[] args){

        int n = 5;
        int[][] edges = {{1,2,3},{1,3,3},{2,3,1},{1,4,2},{5,2,2},{3,5,1},{5,4,10}};
        Solution s = new Solution();
        System.out.println(s.countRestrictedPaths(n, edges));

    }

    public int countRestrictedPaths(int n, int[][] edges) {
        for(int[] e: edges){
            map.computeIfAbsent(e[0], x -> new ArrayList<>()).add(new int[] { e[1], e[2]}); // create graph with weights
            map.computeIfAbsent(e[1], x -> new ArrayList<>()).add(new int[] { e[0], e[2]});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]); // sort based on weight (Dijkstra's)
        pq.offer(new int[]{n ,0});
        int[] dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[n] = 0;

        while(!pq.isEmpty()){
            int[] curr = pq.poll();
            int node = curr[0];
            int weight = curr[1];

            for(int[] neighbor: map.get(node)) {
                int nei =  neighbor[0];
                int w = weight + neighbor[1];

                if(w < dist[nei]) { //only traverse if this will create a shorter path. At the end we have all the shortest paths for each node from the last node, n.
                    dist[nei] = w;
                    pq.offer(new int[]{ nei, w });
                }
            }
        }
        Integer[] dp = new Integer[n+1];
        return dfs(1, n, dist, dp);
    }

    public int dfs(int node, int end, int[] dist, Integer[] dp){
        if(node == end) return 1;
        if(dp[node] != null) return dp[node];
        long res = 0;
        for(int[] neighbor : map.get(node)){
            int nei = neighbor[0];
            if(dist[node] > dist[nei] ){ // use our calculations from Dijkstra's to determine if we can travale to a neighbor.
                res = (res + (dfs(nei, end, dist, dp)) % mod);
            }
        }
        res = (res % mod);
        return dp[node] = (int) res; // memoize for looking up vlaues that already been computed.

    }


}