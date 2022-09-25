/*
 * https://leetcode.com/problems/closest-dessert-cost/
 * https://leetcode.com/problems/closest-dessert-cost/discuss/1085792/Java-Backtracking
 */

class Solutiondotvikrant_pc {

    int result;

    public static void main(String[] args){

        int[] baseCosts = {1,7}, toppingCosts = {3,4};
        int target = 10;
        Solutiondotvikrant_pc S = new Solutiondotvikrant_pc();
        System.out.println(S.closestCost(baseCosts, toppingCosts, target));

    }

    public int closestCost(int[] baseCosts, int[] toppingCosts, int target) {
        result = baseCosts[0];
        for(int base: baseCosts){
            helper(base, toppingCosts, 0, target);

        }
        return result;
    }

    private void helper(int current, int[] toppingCosts, int index, int target) {
        if(Math.abs(target-current) < Math.abs(target-result) || Math.abs(target-current) == Math.abs(target-result) && current < result)
        {
            result = current;
        }

        if(index == toppingCosts.length || current >= target) return;
        helper(current, toppingCosts, index + 1, target);
        helper(current + toppingCosts[index], toppingCosts, index + 1, target);
        helper(current + toppingCosts[index]*2, toppingCosts, index + 1, target);
    }

}