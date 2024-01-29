package com.mycompany.leetcode.grind75.week8.BasicCalculator;

import java.util.Stack;

public class BasicCalculatorSouthpenguin {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<Integer>();
        int result = 0;
        int number = 0;
        int sign = 1;
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isDigit(c)) {
                number = 10 * number + (int) (c - '0');
            } else if (c == '+') {
                result += sign * number;
                number = 0;
                sign = 1;
            } else if (c == '-') {
                result += sign * number;
                number = 0;
                sign = 1;
            } else if (c == '(') {
                stack.push(result);
                stack.push(sign);
                sign = 1;
                result = 0;
            } else if (c == ')') {
                result += sign * number;
                number = 0;
                result *= stack.pop();
                result += stack.pop();
            }
        }
        if(number != 0 ) result += sign * number;
        return result;
    }

    public static void main(String[] args) {
        String s = " 2-1 + 2 ";
        BasicCalculatorSouthpenguin obj = new BasicCalculatorSouthpenguin();
        System.out.println(obj.calculate(s));

    }
}
