/*
 * https://leetcode.com/problems/remove-stones-to-minimize-the-total/
 * https://leetcode.com/problems/remove-stones-to-minimize-the-total/discuss/1390274/Java-or-Max-heap-Solution-with-Algorithm-and-Explanation
 */
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

class Solutiondotaayush912 {

    public static void main(String[] args) {

        Solutiondotaayush912 S = new Solutiondotaayush912();
        int[] piles = {5,4,9};
        int k = 2;
        System.out.println(S.minStoneSum(piles, k));

    }

    public int minStoneSum(int[] piles, int k) {
        Queue <Integer> heap = new PriorityQueue<>(new Comparator<Integer>() {
            public int compare (Integer a, Integer b) {
                if (a < b) 
                {
                    return 1;
                } else if (a > b) {
                    return -1;
                } else {
                    return 0;
                }
            }
        });

        for(int val : piles){
            heap.offer(val);
        }
        while(k-- > 0) {
            int stones = heap.poll();
            stones -= (int) (Math.floor (stones / 2));
            heap.offer(stones);
        }
        int sum = 0;
        while(!heap.isEmpty()){
            sum += heap.poll();
        }
        return sum;
    }
}