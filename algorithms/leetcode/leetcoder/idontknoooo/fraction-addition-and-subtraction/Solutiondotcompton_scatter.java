/*
 * 
 * https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/103388/Concise-Java-Solution
 * 
 * https://leetcode.com/problems/fraction-addition-and-subtraction/
 */

import java.util.stream.Stream;

class Solutiondotcompton_scatter{

    public static void main(String[] args){

        Solutiondotcompton_scatter S = new Solutiondotcompton_scatter();
        String expression = "-1/2+1/2";
        System.out.println(S.fractionAddition(expression));

    }

    public String fractionAddition(String expression) {        
        String[] fracs = expression.split("(?=[-+])"); // splits input string into individual fractions
        String res = "0/1";
        for(String frac : fracs) res = add(res, frac); // add all fractions together
        return res;
    }

    public String add(String frac1, String frac2) {
        int[] f1 =  Stream.of(frac1.split("/")).mapToInt(Integer::parseInt).toArray(),
              f2 = Stream.of(frac2.split("/")).mapToInt(Integer::parseInt).toArray();
        int number = f1[0]*f2[1] + f1[1]*f2[0], denom = f1[1] * f2[1];
        String sign = "";
        if(number < 0) {sign = "-"; number *= -1;}
        return sign + number/gcd(number,denom) + "/" + denom/gcd(number, denom); // construct reduced fraction)

    }
    // Computes gcd using Euclidean algorithm
    public int gcd(int x, int y) { return x == 0 || y == 0 ? x + y : gcd(y, x % y); }
}