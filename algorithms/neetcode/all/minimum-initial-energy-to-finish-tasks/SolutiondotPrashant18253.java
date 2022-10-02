/*
 * 
 * https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
 * https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/discuss/1300167/Greedy-solution-sorting
 */
import java.util.*;

class SolutiondotPrashant18253 {

    public static void main(String[] args) {

        SolutiondotPrashant18253 S = new SolutiondotPrashant18253();

        int[][] tasks = {{1,3},{2,4},{10,11},{10,12},{8,9}};
        
        System.out.println(S.minimumEffor(tasks));

    }

    public int minimumEffor(int[][] tasks) {
        Arrays.sort(tasks, new Comparator<int[]>() {

            @Override
            public int compare(int[] a, int[] b) {
                return (b[1]-b[0]) - (a[1]-a[0]);
            }
        });

        int sum = 0, max = 0;
        for(int i = 0; i < tasks.length; i++){
            max = Math.max(max, sum+tasks[i][1]);
            sum += tasks[i][0];
        }
        return max;

    }

}