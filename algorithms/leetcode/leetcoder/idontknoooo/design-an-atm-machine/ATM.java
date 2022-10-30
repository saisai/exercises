/*
 * 
 * https://leetcode.com/problems/design-an-atm-machine/
 * https://leetcode.com/problems/design-an-atm-machine/discuss/1953723/JAVA-Simple-Solution
 */

import java.util.Arrays;

public class ATM {

    long[] denoms = {20, 50, 100, 200, 500};
    long[] stores;

    
    public static void main(String[] args) {
        ATM obj = new ATM();
        int[] banknotesCount =  {0,0,1,2,1};
        obj.deposit(banknotesCount);
        int[] param_2 = obj.withdraw(600);
        System.out.println(Arrays.toString(param_2));

        


    }

    public ATM() {
        stores = new long[5];
    }

    public void deposit(int[] banknotesCount) {
        for(int i = 0; i < 5; i++) {
            stores[i] += banknotesCount[i];
        }
    }

    public int[] withdraw(int amount) {
        long[] ans = new long[5];
        int index = 4;
        while(amount > 0 && index >= 0) {
            long takethismany = Math.min(amount / denoms[index], stores[index]);
            ans[index] = takethismany;
            amount -= takethismany * denoms[index];
            index--;
        }

        if(amount != 0){
            return new int[]{-1};
        } else {
            for(int i = 0; i < 5; i++) {
                stores[i] -= ans[i];
            }
            return Arrays .stream(ans).mapToInt(i -> (int) i).toArray();        }
    }

    
}
