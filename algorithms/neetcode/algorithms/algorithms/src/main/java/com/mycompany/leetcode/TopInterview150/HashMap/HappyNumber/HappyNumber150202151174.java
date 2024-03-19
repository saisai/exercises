package com.mycompany.leetcode.TopInterview150.HashMap.HappyNumber;

public class HappyNumber150202151174 {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;

        do {
            slow = square(slow);
            fast = square((square(fast)));
        } while(slow != fast);

        return slow == 1;
    }

    public int square(int num) {
        int ans = 0;
        while(num > 0) {
            int remainder = num % 10;
            ans += remainder * remainder;
            num /= 10;
        }
        return ans;
    }

    public static void main(String[] args) {
        HappyNumber150202151174 obj = new HappyNumber150202151174();
        System.out.println(obj.isHappy(19));
    }
}
