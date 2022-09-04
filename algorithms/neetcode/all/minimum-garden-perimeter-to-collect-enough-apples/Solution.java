/*
 * https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/discuss/1375450/Java-O(NlogN)-Step-by-Step-Explanation
 * https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/discuss/?currentPage=1&orderBy=most_votes&query=
 */

class Solution {
    public static void main(String[] args){

        long neededApples = 1;
        Solution S = new Solution();
        System.out.println(S.minimumPerimeter(neededApples));

    }

    public long minimumPerimeter(long neededApples) {
        long left = 1;
        long right = 100000;
        while(left < right){
            long r = (left + right) / 2;
            if(2 * r * (r + 1) * (2 * r + 1) >= neededApples) {
                right = r;
            } else {
                left = r + 1;
            }
        }
        return left * 8;
    }
}